
import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import config
from handlers.h01_start import router as start_router


# Настройка логирования
logging.basicConfig(level=logging.INFO if not config.DEBUG else logging.DEBUG)
logger = logging.getLogger(__name__)


async def main():
    """Точка входа в приложение."""
    # Создаем объект бота
    bot = Bot(token=config.BOT_TOKEN)

    # Создаем диспетчер
    dp = Dispatcher()

    # Подключаем роутер с командой /start
    dp.include_router(start_router)

    logger.info("Бот запущен. Администраторы: %s", config.ADMIN_IDS)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error("Ошибка при работе бота: %s", e)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())