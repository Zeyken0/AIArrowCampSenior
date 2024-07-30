import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.markdown import hlink
from config import BOT_TOKEN
from llm import GigaChatInterface


model = GigaChatInterface()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class Form(StatesGroup):
    waiting_for_request = State()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = ["Информация о проекте", "Задачи", "Идеи"]
    keyboard.add(*buttons)
    await message.answer("<b>Привет!</b>👋\n"
                         "Я твой персональный помощник в работе с командой. 🤖\n"
                         "Благодаря мне ты можешь:\n"
                         "1. Получить краткую выжимку по своему проекту для дальнейшей презентации;\n"
                         "2. Структурировать свои идеи и мысли относительно проектной задачи;\n"
                         "3. Конкретизировать и структуризировать задачи, возникаемые во время работы над проектом.\n"
                         f"{hlink('AI-Arrow', 'ai-arrow-camp.com')}",
                         reply_markup=keyboard, parse_mode="html")


@dp.message_handler(lambda message: message.text in ["Информация о проекте", "Задачи", "Идеи"])
async def process_option(message: types.Message, state: FSMContext):
    await state.update_data(selected_option=message.text)
    await Form.waiting_for_request.set()
    await message.answer("Пожалуйста, введите ваш запрос...")


@dp.message_handler(state=Form.waiting_for_request)
async def process_request(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    selected_option = user_data.get('selected_option')
    user_request = message.text
    if selected_option == "Информация о проекте":
        response = model.project_struct(user_request)
    elif selected_option == "Задачи":
        response = model.task_struct(user_request)
    elif selected_option == "Идеи":
        response = model.idea_struct(user_request)
    await message.answer(response)
    await state.finish()
