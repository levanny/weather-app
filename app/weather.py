import httpx
import os

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

async def get_weather(city: str):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            return {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"]
            }
        else:
            return {"error": "City not found or API error."}
