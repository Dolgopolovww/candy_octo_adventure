from icecream import ic
from sqlalchemy import create_engine, desc, null
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from configuration_data.config import postgres_info as pi
from utils.db.creating_tables import User, Account_balance, Cost_history

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

def add_items(telegram_id, date, purchase_name, sum, store_name):
    try:
        item = Cost_history(user_id=telegram_id, date=date,
                            purchase_name=purchase_name, sum=sum,
                            store_name=store_name)
        session.add(item)
        session.commit()
        recalculate_balance(telegram_id)
    except Exception as ex:
        #ic(ex)
        session.rollback()
        return "error"

def recalculate_balance(telegram_id):
    try:
        last_balance = session.query(Account_balance).filter(Account_balance.user_id == telegram_id).first().balance
        last_purchase = session.query(Cost_history).filter(Cost_history.user_id == telegram_id).order_by(desc(Cost_history.id)).first().sum
        balance = last_balance-last_purchase
        #print(last_balance, last_purchase, balance)
        session.query(Account_balance).filter(Account_balance.user_id == telegram_id).update({Account_balance.balance:balance})
        session.commit()
    except Exception as ex:
        #ic(ex)
        pass

