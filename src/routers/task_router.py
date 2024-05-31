from fastapi import APIRouter, Depends
from src.services.task_service import TaskService
from src.guards.auth_bearer import JWTBearer

router = APIRouter(prefix="/task", tags=["task"])


@router.post("/create/{columnId}/{content}", dependencies=[Depends(JWTBearer())])
async def create_task(columnId: int, content: str):
    return await TaskService.create_task(columnId, content)


@router.put("/update/{id}/{content}", dependencies=[Depends(JWTBearer())])
async def update_task(id: int, content: str):
    return await TaskService.update_task(id, content)


@router.get("/all/{columnId}", dependencies=[Depends(JWTBearer())])
async def return_tasks(columnId: int):
    return await TaskService.return_all_tasks(columnId)
