import asyncio
from app.db.database import Base, engine

async def create_and_show_tables():
    async with engine.begin() as conn:
        # Create tables in database
        await conn.run_sync(Base.metadata.create_all)
        print("Tables created!")

    # Verify tables in the database
    async with engine.begin() as conn:
        tables = await conn.run_sync(lambda sync_conn: list(Base.metadata.tables.keys()))
        print("Current tables in database:", tables)

if __name__ == "__main__":
    asyncio.run(create_and_show_tables())
