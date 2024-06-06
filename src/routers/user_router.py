from fastapi import APIRouter, Depends
from src.services.user_service import UserService
from src.guards.auth_bearer import JWTBearer

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/{id}", dependencies=[Depends(JWTBearer())])
async def get_user_by_id(id: int):
    return await UserService.find_user_by_id(id)
