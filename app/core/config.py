from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    cities: List[str] = ["kutaisi", "batumi", "samtredia", "tbilisi", "zugdidi"]
    api_key: str
    base_url: str = "https://api.openweathermap.org/data/2.5/weather"
    database_url: str
    interval: int = 60

    class Config:
        env_file = ".env"

settings = Settings()
