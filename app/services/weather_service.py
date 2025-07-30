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
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "sunrise": data["sys"]["sunrise"],
        "sunset": data["sys"]["sunset"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"]
    }
