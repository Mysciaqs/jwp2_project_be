from fastapi import HTTPException
import bcrypt
from src.database.prisma import User
from src.schemas.user_schema import CreateUser


class UserService:
    @staticmethod
    async def create_user(user_schema: CreateUser):
        user = await User.prisma().find_unique(where={"email": user_schema.email})
        if user:
            raise HTTPException(status_code=409, detail="Email duplicated")
        new_user = await User.prisma().create(
            data={
                "email": user_schema.email,
                "password": bcrypt.hashpw(
                    user_schema.password.encode("utf-8"), bcrypt.gensalt()
                ).decode("utf-8"),
                "firstName": user_schema.firstName,
                "lastName": user_schema.lastName,
            }
        )
        return new_user

    @staticmethod
    async def find_user_by_email(email: str):
        return await User.prisma().find_unique(where={"email": email})

    @staticmethod
    async def find_user_by_id(id: int):
        return await User.prisma().find_unique(where={"id": id})
