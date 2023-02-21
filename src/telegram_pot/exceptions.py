class ChatHasOpenProcess(Exception):
    def __init__(self, chat_id: int) -> None:
        self.chat_id = chat_id
        super()
