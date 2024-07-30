from langchain_community.chat_models import GigaChat
from config import GIGACHAT_CREDENTIALS

chat = GigaChat(
    model='GigaChat',
    credentials=GIGACHAT_CREDENTIALS,
)
#, verify_ssl_certs=False, stream = True

from langchain.schema import HumanMessage, SystemMessage

messages = [
    HumanMessage(content='Привет!')
]

print(chat.get_models())
