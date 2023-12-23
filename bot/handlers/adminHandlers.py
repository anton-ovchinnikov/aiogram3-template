from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from bot.callbacks.AdminCallbackFactory import AdminCallbackFactory, AdminAction
from bot.filters.IsAdmin import IsAdmin
from bot.keyboards.adminKeyboards import get_admin_keyboard
from bot.labels.messages import ADMIN_MSG, ADMIN_ALERT

router = Router()

router.message.filter(IsAdmin())
router.callback_query.filter(IsAdmin())


@router.message(Command('admin'))
async def admin_cmd_handler(message: Message) -> None:
    await message.answer(text=ADMIN_MSG, reply_markup=get_admin_keyboard())
    await message.delete()


@router.callback_query(AdminCallbackFactory.filter(F.action == AdminAction.admin_action_1))
async def admin_action_1_handler(query: CallbackQuery) -> None:
    await query.answer(text=ADMIN_ALERT, show_alert=True)
