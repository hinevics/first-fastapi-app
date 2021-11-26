from datetime import datetime
from enum import Enum

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.exc.declarative import declarative_base

from app.config import DATABASE_URL


Base = declarative_base()


class StatusStream(Enum):
    PLANED = 'planed'
    ACTIVE = 'acrive'
    CLOSED = 'closed'


def connect_db():
    engine = create_engine(DATABASE_URL, connect_args={})
    session = Session(bind=engine.connect())
    return session


class User:
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, )
    password = Column(String, )
    first_name = Column(String)
    last_name = Column(String)
    nicknam = Column(String)
    created_at = Column(String, default=datetime.utcnow())


class Stream(Base):
    __tablename__ = 'stream'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_id'))
    title = Column(String)
    topic = Column(String)
    status = Column(String, default=StatusStream.PLANED.value)
    created_at = Column(String, default=datetime.utcnow())


class AuthToken(Base):
    __tablename__ = 'auth_token'
    id = Column(Integer, primary_key=True)
    token = Column(String)
    user_id = Column(Integer, ForeignKey('user_id'))
    created_at = Column(String, default=datetime.utcnow())
