from aiogram.dispatcher.filters.state import StatesGroup, State


class AddItems(StatesGroup):
    date = State()
    purchase_name = State()
    sum = State()
    store_name = State()


