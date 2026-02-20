import os
import re
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


# 1. Загрузка и очистка конфиденциальных данных из переменных окружения
DB_USER = clean_value(os.getenv("DB_USER", "postgres"))
DB_PASSWORD = clean_value(os.getenv("DB_PASSWORD", "password"))
DB_HOST = clean_value(os.getenv("DB_HOST", "localhost"))
DB_PORT = clean_value(os.getenv("DB_PORT", "5432"))
DB_NAME = clean_value(os.getenv("DB_NAME", "my_db"))

# 2. Формирование строки подключения (DSN)
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 3. Создание движка SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Вывод SQL-запросов (отключить в продакшене)
    pool_pre_ping=True,
)

# 4. Фабрика сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Базовый класс для моделей
Base = declarative_base()