from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.callbacks.AdminCallbackFactory import AdminCallbackFactory, AdminAction
from bot.labels.buttons import ADMIN_BTN, CLOSE_BTN


def get_admin_keyboard() -> InlineKeyboardMarkup:
    admin_action_1_cb = AdminCallbackFactory(action=AdminAction.admin_action_1).pack()
    keyboard = [
        [InlineKeyboardButton(text=ADMIN_BTN, callback_data=admin_action_1_cb)],
        [InlineKeyboardButton(text=CLOSE_BTN, callback_data='close')]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup
