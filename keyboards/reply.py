from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_menu_kb():
    """Клавиатура главного меню типа reply"""
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="Оформить заказ✅"))
    builder.add(KeyboardButton(text="Заказы📦"))
    builder.adjust(2)  # 2 кнопки в строке
    return builder.as_markup(resize_keyboard=True)


def to_menu_main_kb():
    """Клавиатура с одной кнопкой 'Главное меню🏠'"""
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="Главное меню🏠"))
    return builder.as_markup(resize_keyboard=True)
