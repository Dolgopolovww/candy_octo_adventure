from icecream import ic
from sqlalchemy import create_engine, Numeric
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Text, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.schema import DropTable
from sqlalchemy.ext.compiler import compiles
from sqlalchemy import text

from configuration_data.config import postgres_info as pi

engine = create_engine(f"postgresql+psycopg2://{pi['user']}:{pi['password']}@{pi['host']}:{pi['port']}/{pi['db']}", echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    telegram_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    surname = Column(String(255))
    username = Column(String(255))

    user_id_account_balance = relationship("Account_balance")
    user_id_cost_history = relationship("Cost_history")

class Account_balance(Base):
    __tablename__ = "account balance"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.telegram_id"))
    balance = Column(Integer)

class Cost_history(Base):
    __tablename__ = "cost history"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.telegram_id"))
    date = Column(Date)
    purchase_name = Column(String(255))
    sum = Column(Integer)
    store_name = Column(String(255))


#Base.metadata.drop_all(engine)
#Base.metadata.create_all(engine)