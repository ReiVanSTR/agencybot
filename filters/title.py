from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
import typing
class TitileLen(BoundFilter):
    key = 'message_len'

    def __init__(self, message_len: typing.Union[typing.Iterable, str]):
        if isinstance(message_len, str):
            message_len = [message_len]
        self.message_len = message_len

    def check(self, message: types.Message) -> bool:
        return 4 < len(message.text) < 25