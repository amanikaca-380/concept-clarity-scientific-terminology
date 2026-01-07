from sqlalchemy import Column, Integer, String
from backend.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

class SearchHistory(Base):
    __tablename__ = "search_history"

    id = Column(Integer, primary_key=True, index=True)
    term = Column(String, index=True)
    user_email = Column(String, index=True)
    searched_at = Column(DateTime, default=datetime.utcnow)
