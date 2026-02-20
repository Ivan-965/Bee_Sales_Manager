from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database.base import Base


class Order(Base):
    """
    Модель заказа. Связана с пользователем через user_id.
    """
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # Связь с User
    quantity = Column(Integer, nullable=False)  # Количество товара
    breed = Column(String(100), nullable=False)  # Порода (например, животного или растения)
    comment = Column(Text, nullable=True)       # Комментарий к заказу
    status = Column(Enum('pending', 'confirmed', 'shipped', 'cancelled', name='order_status'),
                    default='pending', nullable=False)  # Статус заказа

    # Обратная связь: один пользователь — много заказов
    user = relationship("User", back_populates="orders")

    def __repr__(self):
        return f"<Order(id={self.id}, user_id={self.user_id}, breed={self.breed!r}, status={self.status})>"