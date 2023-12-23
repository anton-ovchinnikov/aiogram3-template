from aiogram.filters import Filter
from aiogram.types import TelegramObject

from configreader import config


class IsAdmin(Filter):
    async def __call__(self, event: TelegramObject):
        return event.from_user.id == config.ADMIN_ID
