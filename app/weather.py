import httpx
import os
from typing import Optional

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

async def get_weather_data(city: str):
    if not API_KEY:
        raise EnvironmentError("Weather API_KEY not found in the environment variables")
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    async with httpx.AsyncClient() as client:

        try:
            response = await client.get(BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
            return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
            }
        except httpx.HTTPStatusError as e:
            return{"error": f"API returned {e.response.status_code}"}
        except  Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
