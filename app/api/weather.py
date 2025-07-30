from fastapi import APIRouter, HTTPException
from app.services.weather_service import fetch_weather

router = APIRouter()

@router.get("/{city}")
async def get_weather(city: str):
    try:
        return await fetch_weather(city)
    except HTTPException as e:
        raise e
