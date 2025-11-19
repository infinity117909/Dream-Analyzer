from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from datetime import datetime
from database import Base

# Create User, Symbol, and Dream models

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    password_hash = Column(Text)

class Symbol(Base):
    __tablename__ = "symbols"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    symbol = Column(String(100))
    personal_meaning = Column(Text)
    category = Column(String(50))

class Dream(Base):
    __tablename__ = "dreams"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(Text)
    date = Column(DateTime, default=datetime.utcnow)
    mood = Column(String(20))
