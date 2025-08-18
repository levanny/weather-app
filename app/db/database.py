# app/db/database.py

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Async engine for PostgreSQL
engine = create_async_engine(
    settings.database_url,
    echo=True  # Optional: logs SQL queries for debugging
)

# Async session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependency to get DB session in FastAPI endpoints
async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

get_db = get_session()
