import os
import sys
import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import pool

# add project root (so imports below work when Alembic runs)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.db.database import Base  # target_metadata
from app.core.config import settings
from app.db.models import Weather

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def _get_db_url():
    # Prefer CLI: alembic -x db_url=... upgrade head
    xargs = context.get_x_argument(as_dictionary=True)
    if "db_url" in xargs and xargs["db_url"]:
        return xargs["db_url"]

    # Then environment: export DATABASE_URL=...
    if os.getenv("DATABASE_URL"):
        return os.environ["DATABASE_URL"]

    # Finally, app settings (.env via pydantic-settings)
    if getattr(settings, "database_url", None):
        return settings.database_url

    raise RuntimeError("Database URL not provided. Use -x db_url=..., or set DATABASE_URL, or set settings.database_url.")

def run_migrations_offline():
    url = _get_db_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )
    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,
    )
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    url = _get_db_url()
    connectable = create_async_engine(url, poolclass=pool.NullPool, future=True)
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()

if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
