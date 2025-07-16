from fastapi import FastAPI
from app.weather import get_weather


app = FastAPI()

@app.get("/weather")
async def read_weather(city: str):
    weather = await get_weather(city)
    return weather