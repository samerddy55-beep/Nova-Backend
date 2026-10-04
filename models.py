from pydantic import BaseModel, Field
from typing import Optional


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: str = Field(min_length=5, max_length=150)
    password: str = Field(min_length=6, max_length=200)


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str
    plan: str
    active: bool


class LoginRequest(BaseModel):
    email: str
    password: str


class AIRequest(BaseModel):
    message: str = Field(min_length=1, max_length=10000)
    model: Optional[str] = "gpt-oss"


class AIResponse(BaseModel):
    success: bool
    model: str
    response: str
