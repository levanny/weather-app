import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase, declared_attr
from sqlalchemy import MetaData

metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

class Base(DeclarativeBase):
    metadata = metadata
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:FantasticFox@db:5432/postgres"
)

engine = create_async_engine(DATABASE_URL, echo=True, future=True)

AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session