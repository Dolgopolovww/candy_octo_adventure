from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import callback_data
from aiogram.utils.callback_data import CallbackData


navigation_menu = CallbackData("show_menu", "action")
navigation_menu_keyboard = InlineKeyboardMarkup(row_width=2)

navigation_menu_keyboard.insert(InlineKeyboardButton(text="Главное меню", callback_data="show_menu:main_menu"))




navigation_menu_opt = CallbackData("show_menu", "action")
navigation_menu_opt_keyboard = InlineKeyboardMarkup(row_width=2)

navigation_menu_opt_keyboard.insert(InlineKeyboardButton(text="Назад", callback_data="show_menu:main_menu"))