import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker, Session
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(os.getenv("DB_URL"))
SessionLocal = sessionmaker(autoflush=False, bind=engine)
connection = engine.connect()
metadata = MetaData()

class Base(DeclarativeBase):
    pass

class ToDo(Base):
    __tablename__ = "Todo"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    completed: Mapped[bool] = mapped_column()

flag = True

def create_table():
    global flag
    if flag:
        Base.metadata.create_all(engine)
        flag = False
