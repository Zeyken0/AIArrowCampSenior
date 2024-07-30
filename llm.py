from langchain_community.chat_models import GigaChat
from langchain.schema import HumanMessage, SystemMessage
from config import GIGACHAT_CREDENTIALS


class LLMObject:
    def project_struct(self, content: str) -> str:
        return 'Basic return'

    def idea_struct(self, content: str) -> str:
        return 'Basic return'

    def task_struct(self, content: str) -> str:
        return 'Basic return'


class GigaChatInterface(LLMObject):
    def __init__(self):
        self._model = GigaChat(
            model='GigaChat',
            credentials=GIGACHAT_CREDENTIALS,
            verify_ssl_certs=False
        )

    def project_struct(self, content: str) -> str:
        system_message = SystemMessage(
            content="Ты — эксперт по структуризации информации о проектах Структурируй информацию,"
                    " не добавляй ничего лишнего"
        )

        specifier_prompt = [
            system_message,
            HumanMessage(
                content=f"""{content}"""
            ),
        ]
        result = self._model(specifier_prompt).content
        return result

    def idea_struct(self, content: str) -> str:
        system_message = SystemMessage(
            content="Ты — эксперт по структуризации информации о идеях Структурируй информацию,"
                    " не добавляй ничего лишнего"
        )

        specifier_prompt = [
            system_message,
            HumanMessage(
                content=f"""{content}"""
            ),
        ]
        result = self._model(specifier_prompt).content
        return result

    def task_struct(self, content: str) -> str:
        system_message = SystemMessage(
            content="Ты — эксперт по структуризации информации о задачах. Структурируй информацию,"
                    " не добавляй ничего лишнего"
        )

        specifier_prompt = [
            system_message,
            HumanMessage(
                content=f"""{content}"""
            ),
        ]
        result = self._model(specifier_prompt).content
        return result
