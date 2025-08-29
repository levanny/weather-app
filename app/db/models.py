from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from app.db.database import Base

class Weather(Base):
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    temperature = Column(Float)
    feels_like = Column(Float)
    humidity = Column(Float)
    wind_speed = Column(Float)
    sunrise = Column(Integer)
    sunset = Column(Integer)
    description = Column(String)
    icon = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)