from fastapi import APIRouter
from src.routers.user_router import router as userRouter
from src.routers.auth_router import router as authRouter

api = APIRouter()
api.include_router(userRouter)
api.include_router(authRouter)

__all__ = ["api"]
