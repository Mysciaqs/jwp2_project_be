from fastapi import FastAPI, responses
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from src.database.prisma import prisma
from src.routers import api as api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await prisma.connect()
    yield
    await prisma.disconnect()


def create_app():
    app = FastAPI(lifespan=lifespan)
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT"],
        allow_headers=["*"],
        allow_origins=["http://localhost:3000"],
    )
    app.include_router(api_router, prefix="/api")
    return app


app = create_app()


@app.get("/")
async def root():
    return responses.RedirectResponse(url="/docs")
