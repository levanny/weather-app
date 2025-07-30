from fastapi import FastAPI
from app.api.weather import router as weather_router

app = FastAPI(title="Pro Weather App")
app.include_router(weather_router, prefix="/weather", tags=["Weather"])
