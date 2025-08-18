from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime
import asyncio

from app.services.weather_service import fetch_weather
from app.db.models import Weather
from app.db.database import engine, get_session
from app.core.config import settings

app = FastAPI(title="Weather App")


@app.on_event("startup")
async def startup():
    # Create tables if not exist
    async with engine.begin() as conn:
        await conn.run_sync(Weather.metadata.create_all)

        asyncio.create_task(weather_scheduler())


@app.post("/weather/fetch")
async def fetch_and_store_weather(session: AsyncSession = Depends(get_session)):
    results = []
    for city in settings.cities:
        data = await fetch_weather(city)
        session.add(Weather(**data))
        results.append(data)
    await session.commit()
    return results

async def weather_scheduler():
    interval = 60
    while True:
        try:
            await fetch_and_store_weather()
        except Exception as e:
            print(f"Error fetching weather: {e}")
        await asyncio.sleep(interval)

