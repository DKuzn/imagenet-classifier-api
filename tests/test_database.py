import os
import sys

from api.db.database import DbWrapper
import pytest
import asyncio

pytest_plugins = ('pytest_asyncio',)

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


@pytest.mark.asyncio
async def test_db():
    data = await DbWrapper.get_users(DbWrapper)
    print(data)
    assert data == {"name": "name1", "surname": "surname1"}
