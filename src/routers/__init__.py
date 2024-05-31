from fastapi import APIRouter
from src.routers.user_router import router as userRouter
from src.routers.auth_router import router as authRouter
from src.routers.column_router import router as columnRouter
from src.routers.task_router import router as taskRouter

api = APIRouter()
api.include_router(userRouter)
api.include_router(authRouter)
api.include_router(columnRouter)
api.include_router(taskRouter)

__all__ = ["api"]
