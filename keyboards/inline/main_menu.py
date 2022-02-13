from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import callback_data
from aiogram.utils.callback_data import CallbackData


main_menu = CallbackData("show_menu", "action")
mm_keybord = InlineKeyboardMarkup(row_width=2)
add_items = InlineKeyboardButton(text="Добавить", callback_data="show_menu:add_items")
mm_keybord.insert(add_items)
delete_items = InlineKeyboardButton(text="Удалить запись", callback_data="show_menu:delete_items")
mm_keybord.insert(delete_items)
see_spending = InlineKeyboardMarkup(text="Посмотреть траты", callback_data="show_mennu:see_spending")
mm_keybord.insert(see_spending)