from fastapi import HTTPException
import bcrypt
import jwt
import os
import time
from datetime import datetime, timezone, timedelta
from src.database.prisma import User
from src.schemas.auth_schema import LoginUser
from src.services.user_service import UserService


class AuthService:
    @staticmethod
    async def login_user(login_schema: LoginUser):
        user = await UserService.find_user_by_email(login_schema.username)
        if user:
            if bcrypt.checkpw(
                login_schema.password.encode("utf-8"), user.password.encode("utf-8")
            ):
                now = datetime.now(timezone.utc)
                at_payload = {
                    "sub": user.email,
                    "firstName": user.firstName,
                    "lastName": user.lastName,
                    "iat": now,
                    "exp": now + timedelta(days=7),
                }
                rt_payload = {
                    "sub": user.email,
                    "firstName": user.firstName,
                    "lastName": user.lastName,
                    "iat": now,
                    "exp": now + timedelta(days=7),
                }
                return {
                    "user": user,
                    "tokens": {
                        "accessToken": jwt.encode(
                            at_payload, os.getenv("JWT_AT_SECRET_KEY")
                        ),
                        "refreshToken": jwt.encode(
                            rt_payload, os.getenv("JWT_RT_SECRET_KEY")
                        ),
                    },
                    "expiresIn": time.mktime((now + timedelta(hours=1)).timetuple()),
                }
        raise HTTPException(status_code=403, detail="Wrong credentials")

    @staticmethod
    async def validate_user(login_schema: LoginUser):
        user = await UserService.find_user_by_email(login_schema.username)
        if user and bcrypt.checkpw(
            login_schema.password.encode("utf-8"), user.password.encode("utf-8")
        ):
            return user
        raise HTTPException(status_code=403, detail="Wrong credentials")

    @staticmethod
    async def refresh_token(user):
        now = datetime.now(timezone.utc)
        at_payload = {
            "sub": user.email,
            "firstName": user.firstName,
            "lastName": user.lastName,
            "iat": now,
            "exp": now + timedelta(hours=1),
        }
        rt_payload = {
            "sub": user.email,
            "firstName": user.firstName,
            "lastName": user.lastName,
            "iat": now,
            "exp": now + timedelta(days=7),
        }
        return {
            "user": user,
            "tokens": {
                "accessToken": jwt.encode(at_payload, os.getenv("JWT_AT_SECRET_KEY")),
                "refreshToken": jwt.encode(rt_payload, os.getenv("JWT_RT_SECRET_KEY")),
            },
            "expiresIn": time.mktime((now + timedelta(hours=1)).timetuple()),
        }
