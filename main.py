from contextlib import asynccontextmanager

from fastapi import FastAPI

from config import config
from database import init_database
from api import router
from ai import nova_ai


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("=" * 50)
    print("NOVA BACKEND")
    print("=" * 50)

    print(f"Environment : {config.ENVIRONMENT}")
    print(f"AI Engine   : {config.AI_ENGINE}")
    print(f"AI Model    : {config.AI_MODEL}")

    init_database()

    print("Database    : READY")
    print("API         : READY")
    print("Backend     : ONLINE")

    yield

    print("Nova Backend shutting down...")


app = FastAPI(
    title=config.APP_NAME,
    version=config.VERSION,
    description="Central Backend API for Nova Platform",
    lifespan=lifespan
)


app.include_router(router)


@app.get("/")
def root():

    return {
        "name": config.APP_NAME,
        "version": config.VERSION,
        "status": "online",
        "environment": config.ENVIRONMENT,
        "ai": nova_ai.status()
    }


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": config.APP_NAME,
        "version": config.VERSION
    }
