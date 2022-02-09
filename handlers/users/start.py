from aiogram import types
from utils.loader import dp


async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')