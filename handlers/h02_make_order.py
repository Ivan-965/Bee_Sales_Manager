from aiogram import Router, F
from aiogram.types import Message
from keyboards.inline import make_order_kb
from keyboards.reply import to_menu_main_kb

router = Router()

@router.message(F.text == "Оформить заказ✅")
async def handle_make_order(message: Message):
    """Обработчик сообщения о том что пользователь хочет сделать новый заказ"""
    await message.answer(
        "Вернуться в меню:",
        reply_markup=to_menu_main_kb()
    )
    await message.answer(
        "📦 Вы приступили к оформлению заказа. Выберите действие:",
        reply_markup=make_order_kb()
    )
