"""
получить остаток
"""
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, Message

from utils.loader import dp

from keyboards.inline.main_menu import main_menu


@dp.callback_query_handler(main_menu.filter(action="add_items"))
async def get_phone_number(call: CallbackQuery, callback_data: dict):
    await call.answer(text="")
    await call.message.answer("остаток: 123")

