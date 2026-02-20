from aiogram import types
from keyboards.reply import main_menu_kb  # Импортируем готовую клавиатуру


async def show_main_menu(message: types.Message):
    """
    Отправляет сообщение с текстом и главным меню через send_message.
    """
    await message.bot.send_message(
        chat_id=message.chat.id,
        text="Выберите действие:",
        reply_markup=main_menu_kb()
    )