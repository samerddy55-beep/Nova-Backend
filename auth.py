import hashlib
import secrets

from database import execute, execute_one


def hash_password(password: str) -> str:
    return hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()


def verify_password(password: str, password_hash: str) -> bool:
    return hash_password(password) == password_hash


def create_user(
    username: str,
    email: str,
    password: str
):
    password_hash = hash_password(password)

    existing = execute_one(
        """
        SELECT id
        FROM users
        WHERE username = ? OR email = ?
        """,
        (username, email)
    )

    if existing:
        return None

    execute(
        """
        INSERT INTO users
        (
            username,
            email,
            password_hash
        )
        VALUES (?, ?, ?)
        """,
        (
            username,
            email,
            password_hash
        )
    )

    return execute_one(
        """
        SELECT
            id,
            username,
            email,
            role,
            plan,
            active
        FROM users
        WHERE email = ?
        """,
        (email,)
    )


def authenticate_user(
    email: str,
    password: str
):
    user = execute_one(
        """
        SELECT *
        FROM users
        WHERE email = ?
        """,
        (email,)
    )

    if not user:
        return None

    if not verify_password(
        password,
        user["password_hash"]
    ):
        return None

    if not user["active"]:
        return None

    return user


def create_token():
    return secrets.token_urlsafe(32)
