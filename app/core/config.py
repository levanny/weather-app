from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str
    base_url: str = "https://api.openweathermap.org/data/2.5/weather"
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()
