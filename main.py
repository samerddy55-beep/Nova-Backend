from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# API ROUTER
# ============================================================

app.include_router(router)


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():

    return {
        "name": config.APP_NAME,
        "version": config.VERSION,
        "status": "online",
        "environment": config.ENVIRONMENT,
        "ai": nova_ai.status()
    }


# ============================================================
# HEALTH
# ============================================================

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": config.APP_NAME,
        "version": config.VERSION
    }
