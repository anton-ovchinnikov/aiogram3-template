from enum import Enum

from aiogram.filters.callback_data import CallbackData


class AdminAction(str, Enum):
    admin_action_1: str = 'admin_action_1'


class AdminCallbackFactory(CallbackData, prefix='admin'):
    action: AdminAction
