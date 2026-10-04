import sqlite3
from config import config


def get_connection():
    connection = sqlite3.connect(
        config.DATABASE_URL.replace("sqlite:///", ""),
        check_same_thread=False
    )

    connection.row_factory = sqlite3.Row

    return connection


def init_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT DEFAULT 'user',
            plan TEXT DEFAULT 'free',
            active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            level TEXT NOT NULL,
            action TEXT NOT NULL,
            details TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def execute(query, parameters=()):
    connection = get_connection()

    cursor = connection.execute(
        query,
        parameters
    )

    connection.commit()

    result = cursor.fetchall()

    connection.close()

    return result


def execute_one(query, parameters=()):
    connection = get_connection()

    cursor = connection.execute(
        query,
        parameters
    )

    connection.commit()

    result = cursor.fetchone()

    connection.close()

    return result
