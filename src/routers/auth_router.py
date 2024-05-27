from fastapi import APIRouter
from src.services.user_service import UserService
from src.schemas.user_schema import CreateUser

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
async def register(user: CreateUser):
    return await UserService.create_user(user)


@router.post("/login")
async def login():
    return


@router.post("/refresh")
async def refresh():
    return
