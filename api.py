from fastapi import APIRouter, HTTPException

from config import config
from models import (
    UserCreate,
    LoginRequest,
    AIRequest
)
from auth import (
    create_user,
    authenticate_user,
    create_token
)

router = APIRouter(
    prefix=config.API_PREFIX
)


@router.get("/health")
def health():
    return {
        "status": "online",
        "service": config.APP_NAME,
        "version": config.VERSION
    }


@router.post("/auth/register")
def register(user: UserCreate):

    created_user = create_user(
        user.username,
        user.email,
        user.password
    )

    if not created_user:
        raise HTTPException(
            status_code=409,
            detail="Username or email already exists"
        )

    return {
        "success": True,
        "user": {
            "id": created_user["id"],
            "username": created_user["username"],
            "email": created_user["email"],
            "role": created_user["role"],
            "plan": created_user["plan"],
            "active": bool(created_user["active"])
        }
    }


@router.post("/auth/login")
def login(data: LoginRequest):

    user = authenticate_user(
        data.email,
        data.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_token()

    return {
        "success": True,
        "token": token,
        "user": {
            "id": user["id"],
            "username": user["username"],
            "email": user["email"],
            "role": user["role"],
            "plan": user["plan"]
        }
    }


@router.get("/users")
def users():

    from database import execute

    rows = execute("""
        SELECT
            id,
            username,
            email,
            role,
            plan,
            active,
            created_at
        FROM users
        ORDER BY id DESC
    """)

    return {
        "success": True,
        "users": [
            dict(row)
            for row in rows
        ]
    }


@router.post("/ai/chat")
def ai_chat(data: AIRequest):

    return {
        "success": True,
        "model": data.model or config.AI_MODEL,
        "response": (
            "Nova AI Engine is ready. "
            "The real local model will be connected "
            "in the next stage."
        )
    }
