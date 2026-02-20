from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def make_order_kb():
    """
    Инлайн-клавиатура для выбора способа оформления заказа.
    """
    builder = InlineKeyboardBuilder()

    # Кнопка: Выбрать существующего пользователя
    builder.add(InlineKeyboardButton(
        text="Выбрать существующего пользователя👥",
        callback_data="select_existing_user"
    ))

    # Кнопка: Оформить заказ на нового пользователя
    builder.add(InlineKeyboardButton(
        text="Оформить заказ на нового пользователя➕",
        callback_data="create_new_user"
    ))

    # Размещаем кнопки в один столбец
    builder.adjust(1)

    return builder.as_markup()