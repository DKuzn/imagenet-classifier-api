import os
import sys

from api.db.database import DbWrapper
import pytest
import asyncio

pytest_plugins = ('pytest_asyncio',)

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

def test_db():
    db = DbWrapper()
    data = db.get_users()
    print(data)

    assert data.login == "dkuzn1"

