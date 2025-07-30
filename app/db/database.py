from databases import Database
from app.core.config import settings

database = Database(settings.database_url)
