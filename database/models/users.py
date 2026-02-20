from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=True)

    # Обратная связь: один пользователь — много заказов
    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name!r}, surname={self.surname!r}, phone={self.phone!r})>"