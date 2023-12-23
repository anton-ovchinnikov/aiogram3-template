from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.callbacks.UserCallbackFactory import UserCallbackFactory, UserAction
from bot.labels.buttons import USER_BTN, CLOSE_BTN


def get_menu_keyboard() -> InlineKeyboardMarkup:
    user_action_1_cb = UserCallbackFactory(action=UserAction.user_action_1).pack()
    keyboard = [
        [InlineKeyboardButton(text=USER_BTN, callback_data=user_action_1_cb)],
        [InlineKeyboardButton(text=CLOSE_BTN, callback_data='close')]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup


def get_close_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text=CLOSE_BTN, callback_data='close')]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup
