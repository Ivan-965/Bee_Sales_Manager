from sqlalchemy import text
from sqlalchemy.exc import ProgrammingError, OperationalError
from database.base import engine, Base
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
    Инициализация базы данных: проверка подключения и создание таблиц.
    """
    logger.info("🚀 Начинается инициализация базы данных...")

    # Проверяем подключение
    if not check_connection():
        logger.error("⛔ Остановка инициализации из-за ошибки подключения.")
        return

    try:
        # Создаём все таблицы, если они ещё не существуют
        Base.metadata.create_all(bind=engine)
        logger.info("✅ Все таблицы успешно созданы или уже существуют.")
    except Exception as e:
        logger.error(f"❌ Ошибка при создании таблиц: {e}")
        raise


if __name__ == "__main__":
    init_db()