from src.database.prisma import Task


class TaskService:
    @staticmethod
    async def create_task(columnId: str, content: str):
        return await Task.prisma().create(
            data={"content": content, "columnId": columnId}
        )

    @staticmethod
    async def update_task(id: str, content: str):
        return await Task.prisma().update(where={"id": id}, data={"content": content})

    @staticmethod
    async def return_all_tasks():
        return await Task.prisma().find_many()

    @staticmethod
    async def delete_task(id: str):
        return await Task.prisma().delete(where={"id": id})
