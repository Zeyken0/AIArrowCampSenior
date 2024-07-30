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
        )

    def project_struct(self, content: str) -> str:
        return ''

    def idea_struct(self, content: str) -> str:
        return ''

    def task_struct(self, content: str) -> str:
        return ''


