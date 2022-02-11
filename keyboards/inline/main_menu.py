from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


main_menu = CallbackData("show_menu", "action")
mm_markup = InlineKeyboardMarkup(row_width=2)
user_btn_reg = InlineKeyboardButton(text="Добавить", callback_data="show_menu:add_items")
mm_markup.insert(user_btn_reg)
user_btn_auth = InlineKeyboardButton(text="Остаток", callback_data="show_menu:rest_money")
mm_markup.insert(user_btn_auth)