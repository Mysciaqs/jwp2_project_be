from src.database.prisma import Column


class ColumnService:
    @staticmethod
    async def create_column(userId: int, title: str):
        return await Column.prisma().create(
            data={"title": title, "userId": userId},
        )

    @staticmethod
    async def update_column(id: int, title: str):
        return await Column.prisma().update(where={"id": id}, data={"title": title})

    @staticmethod
    async def return_all_columns(userId: int):
        return await Column.prisma().find_many(where={"userId": userId})
