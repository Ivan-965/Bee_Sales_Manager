from sqlalchemy import text, create_engine
from sqlalchemy.exc import ProgrammingError, OperationalError
from config import *
from database.base import engine, Base, SessionLocal
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Создаём отдельный engine для подключения к postgres (без указания конкретной БД)
db_url_without_db = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}"
# db_url_without_db = str(engine.url).rsplit("/", 1)[0]  # Убираем имя БД
temp_engine = create_engine(db_url_without_db, isolation_level="AUTOCOMMIT")


def create_database():
    """Создаёт базу данных, если она не существует."""
    try:
        with temp_engine.connect() as conn:
            result = conn.execute(
                text(f"S"
                     f"ELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'")
            )
            exists = result.fetchone()
            if not exists:
                conn.execute(text(f'CREATE DATABASE "{DB_NAME}"'))
                logger.info(f"✅ База данных '{DB_NAME}' успешно создана.")
            else:
                logger.info(f"ℹ️ База данных '{DB_NAME}' уже существует.")
    except Exception as e:
        logger.error(f"❌ Ошибка при создании базы данных: {e}")
        raise


def check_connection():
    """Проверяет подключение к базе данных."""
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        logger.info("✅ Подключение к базе данных установлено.")
        return True
    except Exception as e:
        logger.error(f"❌ Не удалось подключиться к базе данных: {e}")
        return False


def init_db():
    """
    Инициализация базы данных: создание БД (если нет), проверка подключения и создание таблиц.
    """
    logger.info("🚀 Начинается инициализация базы данных...")

    create_database()  # Создаём БД, если её нет

    if not check_connection():
        logger.error("⛔ Остановка инициализации из-за ошибки подключения.")
        return

    try:
        Base.metadata.create_all(bind=engine)
        logger.info("✅ Все таблицы успешно созданы или уже существуют.")
    except Exception as e:
        logger.error(f"❌ Ошибка при создании таблиц: {e}")
        raise


if __name__ == "__main__":
    init_db()
