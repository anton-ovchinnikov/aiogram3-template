from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.callbacks.UserCallbackFactory import UserCallbackFactory, UserAction
from bot.database.Database import Database
from bot.keyboards.menuKeyboard import get_menu_keyboard
from bot.labels.messages import START_MSG, USER_MSG

router = Router()


@router.message(CommandStart())
async def start_cmd_handler(message: Message, database: Database) -> None:
    chat_id = message.chat.id
    username = message.from_user.username
    await database.create_user(chat_id=chat_id, username=username)

    firstname = message.from_user.first_name
    await message.answer(text=START_MSG.format(firstname=firstname), reply_markup=get_menu_keyboard())


@router.callback_query(UserCallbackFactory.filter(F.action == UserAction.user_action_1))
async def user_action_1_callback(query: CallbackQuery) -> None:
    await query.message.answer(text=USER_MSG)
    await query.answer()


@router.callback_query(F.data == 'close')
async def close_callback_handler(query: CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    await query.message.delete()
