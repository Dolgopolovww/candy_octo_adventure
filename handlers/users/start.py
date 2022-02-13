import time

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from configuration_data.config import postgres_info as pi
from utils.db.creating_tables import User, Account_balance
from utils.db.func_db import add_user
from utils.loader import dp

from keyboards.inline.main_menu import mm_keybord


engine = create_engine(f"postgresql+psycopg2://{pi['user']}:{pi['password']}@{pi['host']}:{pi['port']}/{pi['db']}")
Session = sessionmaker(bind=engine)
session = Session()


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    """
    стартовая функция бота

    -message.from_user: {"id": 756515243, "is_bot": false, "first_name": "Andrey", "last_name": "Dolgopolov", "username": "dolgopolov_ww", "language_code": "ru"}

     :param message:
    :return: None
    """

    telegram_id = message.from_user.id
    check_user = session.query(User).filter(User.telegram_id == telegram_id).first()
    if check_user == None:
        await message.answer(f"Ну что сладкоежка, решил вести учет своих трат?\n"
                             f"Сейчас я тебя добавлю в систему...")
        time.sleep(3)
        add_user(telegram_id=telegram_id, name=message.from_user.first_name,
                 surname=message.from_user.last_name, username=message.from_user.username)


    balance = session.query(Account_balance).filter(Account_balance.user_id==telegram_id).first().balance
    await message.answer(f'Привет, сладкоежка!\n'
                         f'Остаток: {balance}', reply_markup=mm_keybord)