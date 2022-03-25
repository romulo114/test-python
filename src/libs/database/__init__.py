from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncConnection, AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from settings import POSTGRES_DB_URL

engine: AsyncEngine = create_async_engine(
    POSTGRES_DB_URL,
    convert_unicode=True,
    max_overflow=100,
    future=True
)

db_session = sessionmaker(engine, expire_on_commit=False, autocommit=False, autoflush=False, class_=AsyncSession)


Base = declarative_base()
# Base.query = db_session.query_property()


async def init_db():
    """Initialize the database and flask app"""

    async with engine.begin() as connection:
        await create_tables(connection)
        await populate_default(connection)


async def create_tables(connection: AsyncConnection):
    import apps.models
    await connection.run_sync(Base.metadata.create_all)


async def populate_default(connection: AsyncConnection):
    from .defaults import default_values
    await default_values(connection)


async def drop_tables(connection: AsyncConnection):
    import apps.models
    await connection.run_sync(Base.metadata.drop_all)

