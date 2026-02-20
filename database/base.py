import os
import re
from config import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def clean_value(value: str) -> str:
    """
    Очищает строку от лишних пробелов, табуляций, переносов строк и нулевых байтов.
    """
    if not isinstance(value, str):
        return value
    # Заменяем любые пробельные символы (включая \t, \n, \r, \0) на обычный пробел, убираем дубли
    value = re.sub(r'[\s\u0000]+', ' ', value.strip())
    return value


# DB_USER = clean_value(DB_USER)
DB_PASSWORD = clean_value(os.getenv("DB_PASSWORD"))
DB_HOST = clean_value(os.getenv("DB_HOST"))
DB_PORT = clean_value(os.getenv("DB_PORT"))

DB_NAME = clean_value(os.getenv("DB_NAME"))

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Создание движка SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
)

# Фабрика сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()
