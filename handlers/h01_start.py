from aiogram import Router, types, Bot
from aiogram.filters import Command

from bot_utils.load_admin_ids import load_admin_ids
from keyboards.reply import main_menu_kb

router = Router()

async def show_main_menu(bot : Bot, chat_id: int):
    """Функция для показа главного меню."""

    await bot.send_message(
        chat_id=chat_id,
        text="Выберите действие:",
        reply_markup=main_menu_kb()
    )


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    """
    Обработчик команды /start.
    """
    admin_ids = load_admin_ids()

    if message.from_user.id not in admin_ids:
        await message.answer(
            text="❌ Доступ к этому боту ограничен.\n"
                 "Вы не являетесь администратором."
        )
        return

    # Путь к изображению
    image_path = "media/dispatcher.jpg"

    try:
        # Отправляем фото с подписью
        await message.answer_photo(
            photo=types.FSInputFile(image_path),
            caption=f"🔐 Привет, {message.from_user.full_name}!\n"
                    f"Добро пожаловать в административную панель бота."
        )
        await show_main_menu(bot= message.bot, chat_id=message.chat.id)
    except FileNotFoundError:
        # Если файл не найден — отправляем просто текст
        await message.answer(
            text=f"🔐 Привет, {message.from_user.full_name}!\n"
                 f"Добро пожаловать в административную панель бота.\n"
                 f"(Изображение не найдено)"
        )
        await show_main_menu(bot= message.bot, chat_id=message.chat.id)


    except Exception as e:
        await message.answer(
            text=f"❌ Произошла ошибка при отправке изображения: {e}"
        )
