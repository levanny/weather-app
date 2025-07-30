import httpx
from fastapi import HTTPException
from app.core.config import settings

async def fetch_weather(city: str):
    params = {
        "q": city,
        "appid": settings.api_key,
        "units": "metric"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(settings.base_url, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Weather API error")
        data = response.json()

    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"]
    }
