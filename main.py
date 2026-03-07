import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot_utils.load_admin_ids import load_admin_ids
from config import BOT_TOKEN
from handlers import h01_start, h02_make_order


# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
ADMIN_IDS = load_admin_ids()

async def main():
    """Точка входа в приложение."""
    # Создаем объект бота
    bot = Bot(token=BOT_TOKEN)

    # Создаем диспетчер
    dp = Dispatcher()

    # Подключаем роутер с командой /start
    dp.include_router(h01_start.router)
    dp.include_router(h02_make_order.router)

    logger.info("Бот запущен. Администраторы: %s", ADMIN_IDS)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error("Ошибка при работе бота: %s", e)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())