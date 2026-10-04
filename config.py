import os
from dotenv import load_dotenv

load_dotenv()


class NovaConfig:
    APP_NAME = "Nova Backend"
    VERSION = "1.0.0"
    ENVIRONMENT = os.getenv("NOVA_ENV", "development")

    HOST = os.getenv("NOVA_HOST", "127.0.0.1")
    PORT = int(os.getenv("NOVA_PORT", "8000"))

    API_PREFIX = "/api"

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///./nova.db"
    )

    SECRET_KEY = os.getenv(
        "NOVA_SECRET_KEY",
        "nova-development-secret-change-later"
    )

    AI_ENGINE = os.getenv(
        "NOVA_AI_ENGINE",
        "local"
    )

    AI_MODEL = os.getenv(
        "NOVA_AI_MODEL",
        "gpt-oss"
    )

    DEBUG = ENVIRONMENT == "development"


config = NovaConfig()
