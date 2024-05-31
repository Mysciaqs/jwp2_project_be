from fastapi import APIRouter, Depends
from src.services.column_service import ColumnService
from src.guards.auth_bearer import JWTBearer

router = APIRouter(prefix="/column", tags=["column"])


@router.post("/create/{userId}/{title}", dependencies=[Depends(JWTBearer())])
async def create_column(userId: int, title: str):
    return await ColumnService.create_column(userId, title)


@router.put("/update/{id}/{title}", dependencies=[Depends(JWTBearer())])
async def update_column(id: int, title: str):
    return await ColumnService.update_column(id, title)


@router.get("/all/{userId}", dependencies=[Depends(JWTBearer())])
async def return_columns(userId: int):
    return await ColumnService.return_all_columns(userId)
