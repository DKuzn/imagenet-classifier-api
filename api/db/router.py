from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasicCredentials

from api.auth.auth_service import AuthService
from api.db.database import DbWrapper
from api.db.datamodels import User

router = APIRouter(prefix="/data")
db = DbWrapper()
auth_service = AuthService()


@router.get("/user/{login}", response_model=User | None)
async def get_user(login: str):
    try:
        return db.get_user_by_login(user_login=login)
    except Exception:
        return None


@router.get("/me")
async def get_user1(credentials: Annotated[HTTPBasicCredentials, Depends(auth_service.authenticate)]):
    try:
        return db.get_user_by_login(user_login=credentials.username)
    except Exception:
        return None


@router.post("/user")
async def create_user(user: User):
    try:
        db.create_user(user)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this Login is already existed",
        )


@router.get("/prediction")
async def get_predictions_by_user(credentials: Annotated[HTTPBasicCredentials, Depends(auth_service.authenticate)]):
    try:
        return db.get_predictions_by_user(user_login=credentials.username)
    except Exception:
        return None
