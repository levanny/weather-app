from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio

from app.services.weather_service import fetch_weather
from app.db.models import Weather, Base
from app.db.database import engine, get_session, AsyncSessionLocal
from app.core.config import settings


weather_task = None
app = FastAPI(title="Weather App")


@app.on_event("startup")
async def startup():
    # Create tables if not exist
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Start background weather scheduler
    global weather_task
    weather_task = asyncio.create_task(weather_scheduler())


@app.on_event("shutdown")
async def shutdown():
    # Cancel scheduler on shutdown
    global weather_task
    if weather_task:
        weather_task.cancel()
        try:
            await weather_task
        except asyncio.CancelledError:
            pass


@app.post("/weather/fetch")
async def fetch_and_store_weather(session: AsyncSession = Depends(get_session)):
    """Endpoint: fetch weather for all cities and store in DB"""
    results = []
    for city in settings.cities:
        data = await fetch_weather(city)
        session.add(Weather(**data))
        results.append(data)
    await session.commit()
    return results


async def weather_scheduler():
    """Background task to fetch/store weather every interval"""
    interval = 300
    while True:
        try:
            # Manually manage session (since not in a FastAPI request)
            async with AsyncSessionLocal() as session:
                results = []
                for city in settings.cities:
                    data = await fetch_weather(city)
                    session.add(Weather(**data))
                    results.append(data)
                await session.commit()
                print(f"Fetched weather: {results}")
        except Exception as e:
            print(f"Error fetching weather: {e}")
        await asyncio.sleep(interval)
