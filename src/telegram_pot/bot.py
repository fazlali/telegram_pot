import re
from threading import Thread
from time import sleep, time
from traceback import print_exc
from typing import Callable, List, Any

import requests

from . import exceptions
from .apis import GetUpdates
from .model import API
from .models import Update, Message, CallbackQuery, InlineQuery


class Process:

    def __init__(self, name: str, data: dict = None) -> None:
        self.name = name
        self.data = data or {}
        self.stage: str = 'default'


class TelegramBot:
    API_BASE_URL = 'https://api.telegram.org'

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.update_listeners: dict[str, list[Callable[..., bool]]] = {}
        self.session = requests.Session()
        self.looper: Thread | None = None
        self.processes: dict[int, Process] = {}

    def start(self):
        if not self.looper:
            self.looper: Thread = Thread(target=self._update_loop)
        if not self.looper.is_alive():
            self.looper.start()

    def execute(self, api: API):
        request = api.get_request()
        request.url = f'{self.API_BASE_URL}/bot{self.api_key}/{request.url.strip("/")}'
        response = self.session.send(request.prepare(), timeout=32, allow_redirects=False).json()
        if response['ok']:
            api.set_result(response['result'])
            return api.result
        else:
            raise Exception(response.get('description'))

    def _update_loop(self):
        offset = None
        while True:
            try:
                t = time()
                updates: List[Update] = self.execute(GetUpdates(offset=offset, timeout=30))
                print(1, time() - t)
                for update in updates:
                    t = time()
                    self._new_update(update)
                    print(2, time() - t)
                    offset = update.update_id + 1
            except:
                print_exc()
                sleep(60)

    def _new_update(self, update: Update):
        for update_type, callbacks in self.update_listeners.items():
            if update_type == update.type:
                for callback in callbacks:
                    if callback(update):
                        break

    def new_update(self, update: dict):
        return self._new_update(Update.from_dict(update))

    def add_listener(self, update_type: str, callback: Callable[[Update], bool]):
        listeners = self.update_listeners.get(update_type)
        if listeners is None:
            listeners = []
            self.update_listeners[update_type] = listeners
        listeners.append(callback)

    def create_process(self, chat_id: int, name: str, data: dict = None):
        if self.processes.get(chat_id):
            raise exceptions.ChatHasOpenProcess(chat_id)
        process = Process(name, data)
        self.processes[chat_id] = process
        return process

    def close_current_process(self, chat_id: int):
        process = self.processes.pop(chat_id, None)
        return process

    def on_process(self, process_name: str) \
            -> Callable[[Callable[[Message, Process], Any]], Callable[[Message, Process], bool]]:
        def wrapper(handler: Callable[[Message, Process], bool]):
            def listener(update: Update):
                process = self.processes.get(update.message.chat.id)
                if process and process.name == process_name:
                    return handler(update.message, process)

            self.add_listener('message', listener)
            return handler
        return wrapper

    def on_message(self, pattern: re.Pattern = None, ignore_process: bool = False) \
            -> Callable[[Callable[[Message], Any]], Callable[[Message], bool]]:
        if pattern is None:
            pattern = re.compile('^[^/]')

        def wrapper(handler: Callable[[Message], bool]):
            def listener(update: Update):
                text = update.message.text or update.message.caption
                if text and pattern.match(text):
                    if ignore_process or not self.processes.get(update.message.chat.id):
                        return handler(update.message)

            self.add_listener('message', listener)
            return handler

        return wrapper

    def on_command(self, command_name: str, ignore_process: bool = False) \
            -> Callable[[Callable[[Message], Any]], Callable[[Message], bool]]:
        return self.on_message(
            pattern=re.compile(f'^/{command_name}( |$)'),
            ignore_process=ignore_process
        )

    def on_callback_query(self) \
            -> Callable[[Callable[[CallbackQuery], Any]], Callable[[CallbackQuery], bool]]:
        def wrapper(handler: Callable[[CallbackQuery], bool]):
            def listener(update: Update):
                return handler(update.callback_query)

            self.add_listener('callback_query', listener)
            return handler

        return wrapper

    def on_inline_query(self) \
            -> Callable[[Callable[[InlineQuery], Any]], Callable[[InlineQuery], bool]]:
        def wrapper(handler: Callable[[InlineQuery], bool]):
            def listener(update: Update):
                return handler(update.inline_query)

            self.add_listener('inline_query', listener)
            return handler

        return wrapper
