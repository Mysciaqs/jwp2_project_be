from fastapi import APIRouter
from src.services.user_service import UserService

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/{id}")
async def get_user_by_id(id: int):
    return await UserService.find_user_by_id(id)
