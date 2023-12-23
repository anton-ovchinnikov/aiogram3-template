from sqlalchemy import Column, Integer, BigInteger, Text, DateTime

from bot.database.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    chat_id = Column(BigInteger, nullable=False, unique=True)
    username = Column(Text, nullable=True, unique=True)
    registered_at = Column(DateTime, nullable=False)
