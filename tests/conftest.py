# tests/conftest.py

import pytest_asyncio

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


@pytest_asyncio.fixture
async def async_engine():
    engine = create_async_engine(url="postgresql+asyncpg://postgres:postgres@localhost:5432/postgres")

    yield engine

    await engine.dispose()

@pytest_asyncio.fixture
async def async_session(async_engine): # `async_engine`이라는 매개변수 이름을 사용하면 위의 `async def async_engine` 으로 정의한 fixture가 자동으로 주입됩니다.
    session = AsyncSession(bind=async_engine)

    yield session
    
    await session.close()
