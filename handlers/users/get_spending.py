from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext

from handlers.users.start import bot_main
from keyboards.inline.add_items import adding_options_items, adding_options_keybord
from keyboards.inline.navigator import navigation_menu_keyboard, navigation_menu_opt_keyboard
from states.add_manually_items import AddItems
from utils.db.func_db import add_items, recalculate_balance
from utils.loader import dp

from keyboards.inline.main_menu import main_menu

@dp.callback_query_handler(main_menu.filter(action="see_spending"))
async def all_spending(call: CallbackQuery):

    await call.message.edit_text(f"Траты:\n"
                                 f"*за день:\n"
                                 f"*за неделю:\n"
                                 f"*за месяц:\n"
                                 f"*за пол года:\n"
                                 f"*за год:", reply_markup=navigation_menu_opt_keyboard)
