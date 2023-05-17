from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData
from src.config import DB_USER, DB_PASS, DB_HOST, DB_NAME


DATABASE_URL = "postgresql+asyncpg://%(DB_USER)s:%(DB_PASS)s@%(DB_HOST)s/%(DB_NAME)s"


class Base(DeclarativeBase):
    pass


metadata = MetaData()

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
