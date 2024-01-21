from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext

from api.db.database import DbWrapper
from api.db.datamodels import User

security = HTTPBasic()


class AuthService:
    def __init__(self) -> None:
        self.db = DbWrapper()
        self.crypt_context = CryptContext(["bcrypt"])

    def authenticate(self, credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
        login = credentials.username
        password = credentials.password

        if not self.verify_user(login, password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect login or password",
                headers={"WWW-Authenticate": "Basic"}
            )

        return credentials

    def verify_user(self, login: str, password: str) -> bool:
        try:
            user: User = self.db.get_user_by_login(user_login=login)
            is_login_correct = True
        except Exception:
            is_login_correct = False
            return is_login_correct

        is_password_correct = self.crypt_context.verify(
            password, user.password)

        return is_login_correct and is_password_correct
