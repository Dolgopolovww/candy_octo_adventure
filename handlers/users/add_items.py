from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext

from handlers.users.start import bot_main
from keyboards.inline.add_items import adding_options_items, adding_options_keybord
from states.add_manually_items import AddItems
from utils.db.func_db import add_items, recalculate_balance
from utils.loader import dp

from keyboards.inline.main_menu import main_menu


@dp.callback_query_handler(main_menu.filter(action="add_items"))
async def choice_method(call: CallbackQuery, callback_data: dict):
    await call.message.edit_text(f"Выбери способ добавления:", reply_markup=adding_options_keybord)
    await call.answer(text="")

@dp.callback_query_handler(adding_options_items.filter(action="add_manually"))
async def add_manually_items(call: CallbackQuery):
    await call.message.edit_text(f"Укажите дату покупки")
    await call.answer("")
    await AddItems.date.set()

@dp.message_handler(state=AddItems.date)
async def save_date(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["date"] = message.text
    await message.answer(f"Укажите наименование покупки")
    await AddItems.purchase_name.set()

@dp.message_handler(state=AddItems.purchase_name)
async def save_purchase_name(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["purchase_name"] = message.text
    await message.answer(f"Напиши сумму которую потратил")
    await AddItems.sum.set()

@dp.message_handler(state=AddItems.sum)
async def save_sum(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["sum"] = message.text
    await message.answer(f"В каком магазине??")
    await AddItems.store_name.set()

@dp.message_handler(state=AddItems.store_name)
async def save_store_name(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["store_name"] = message.text
    await state.finish()
    add_items(telegram_id=message.from_user.id, date=data["date"], purchase_name=data["purchase_name"],
              sum=data["sum"], store_name=data["store_name"])
    await message.answer(f"Запись успешно добавлена")
