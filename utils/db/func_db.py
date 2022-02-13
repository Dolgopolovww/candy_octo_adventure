from icecream import ic
from sqlalchemy import create_engine, desc, null
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from configuration_data.config import postgres_info as pi
from utils.db.creating_tables import User, Account_balance

engine = create_engine(f"postgresql+psycopg2://{pi['user']}:{pi['password']}@{pi['host']}:{pi['port']}/{pi['db']}")
Session = sessionmaker(bind=engine)
session = Session()

def add_user(telegram_id, name, surname, username):
    try:
        user = User(telegram_id=telegram_id, name=name, surname=surname, username=username)
        session.add(user)
        session.commit()

        balance = Account_balance(user_id=telegram_id, balance=150)
        session.add(balance)
        session.commit()
    except Exception as ex:
        #ic(ex)
        session.rollback()

