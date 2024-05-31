from src.database.prisma import Task


class TaskService:
    @staticmethod
    async def create_task(columnId: int, content: str):
        return await Task.prisma().create(
            data={"content": content, "columnId": columnId}
        )

    @staticmethod
    async def update_task(id: int, content: str):
        return await Task.prisma().update(where={"id": id}, data={"content": content})

    @staticmethod
    async def return_all_tasks(columnId: int):
        return await Task.prisma().find_many(where={"columnId": columnId})
