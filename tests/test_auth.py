import os
import sys

from api.auth.auth_service import AuthService
import pytest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


def test_auth():
    auth = AuthService()
    assert auth.verify_user("name3", "mypass")