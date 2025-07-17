from fastapi import FastAPI
from app.weather import get_weather_data
from dotenv import load_dotenv


load_dotenv()

app = FastAPI()

@app.get("/weather")
async def read_weather(city: str):
    weather = await get_weather_data(city)
    return weather