from fastapi import APIRouter, Request, Depends
from src.services.user_service import UserService
from src.schemas.user_schema import CreateUser
from src.services.auth_service import AuthService
from src.schemas.auth_schema import LoginUser
from src.guards.auth_bearer import RefreshJWT

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
async def register(user: CreateUser):
    return await UserService.create_user(user)


@router.post("/login")
async def login(credentials: LoginUser):
    return await AuthService.login_user(credentials)


@router.post("/refresh", dependencies=[Depends(RefreshJWT())])
async def refresh(req: Request):
    return await AuthService.refresh_token(req.user)
