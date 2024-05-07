# tests/test_sqlalchemy.py
import pytest

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.mark.asyncio
async def test_db_connection(async_session: AsyncSession):
    result = (await async_session.execute(text("SELECT 1"))).scalar()

    assert result == 1