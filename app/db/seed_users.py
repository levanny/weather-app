import asyncio
from app.db.database import engine
from app.db.models import Users

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

async def seed_users():
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        users = [
            Users(full_name="Alice Smith", email="alice@example.com", password="password1"),
            Users(full_name="Bob Johnson", email="bob@example.com", password="password2"),
            Users(full_name="Charlie Brown", email="charlie@example.com", password="password3"),
            Users(full_name="Diana Prince", email="diana@example.com", password="password4"),
            Users(full_name="Evan Davis", email="evan@example.com", password="password5"),
            Users(full_name="Fiona Clark", email="fiona@example.com", password="password6"),
            Users(full_name="George Miller", email="george@example.com", password="password7"),
            Users(full_name="Hannah Lee", email="hannah@example.com", password="password8"),
            Users(full_name="Ian Scott", email="ian@example.com", password="password9"),
            Users(full_name="Julia Adams", email="julia@example.com", password="password10"),
        ]
        session.add_all(users)
        await session.commit()
        print("10 test users added!")

if __name__ == "__main__":
    asyncio.run(seed_users())
