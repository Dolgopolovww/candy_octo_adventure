from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from utils.loader import dp

from keyboards.inline.main_menu import mm_markup


#5
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, сладкоежка!', reply_markup=mm_markup)