from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import callback_data
from aiogram.utils.callback_data import CallbackData


adding_options_items = CallbackData("show_menu", "action")
adding_options_keybord = InlineKeyboardMarkup(row_width=2)

adding_options_keybord.insert(InlineKeyboardButton(text="Добавить вручную", callback_data="show_menu:add_manually"))
adding_options_keybord.insert(InlineKeyboardButton(text="Выгрузить из Тинкофф", callback_data="show_menu:download_tinkoff"))
adding_options_keybord.insert(InlineKeyboardMarkup(text="Назад", callback_data="show_menu:main_menu"))
