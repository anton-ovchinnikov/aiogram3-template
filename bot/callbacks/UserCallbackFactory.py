from enum import Enum

from aiogram.filters.callback_data import CallbackData


class UserAction(str, Enum):
    user_action_1: str = 'user_action_1'


class UserCallbackFactory(CallbackData, prefix='user'):
    action: UserAction
