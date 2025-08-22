from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Weather(Base):
    __tablename__ = "weather"

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
