from config import (
    DB_HOST_TEST, DB_NAME_TEST, DB_PASS_TEST, DB_PORT_TEST, DB_USER_TEST
    )
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from src.database import metadata, get_async_session
from typing import AsyncGenerator
from src.main import app
import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
import asyncio


# Указываем аддрес тестовой базы
DATABASE_URL_TEST = "postgresql+asyncpg://%(DB_USER_TEST)s:%(DB_PASS_TEST)s@%(DB_HOST_TEST)s/%(DB_NAME_TEST)s"

# Создаем тестовый двигатель
engine_test = create_async_engine(DATABASE_URL_TEST)

# Создаем асинхронный создатель сессий
async_session_maker = async_sessionmaker(engine_test, class_= AsyncSession, expire_on_commit=False)

# Привязываем метаданные к нашему движку, для создания таблиц в тестовой базе данных
metadata.bind = engine_test

# Переписываем зависимости так как используем тестовую базу данных
async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

app.dependency_overrides[get_async_session] = override_get_async_session

# Используем фикстуру для автоматического создания и удаления бд после прогона тестов
@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.drop_all)

# Создаем фикстуру с событийным цыклом для прогона сессии
@pytest.fixture(scope='session')
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

# Создаем синхронный клиент
client = TestClient(app)

# Создаем асинхронный клиент
@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac