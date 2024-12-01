from backend.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    """
      Модель пользователя для базы данных.
      Attributes:
          tablename (str): Название таблицы в базе данных.
          __table_args__ (dict): Аргументы для создания таблицы (extend_existing для избежания ошибок при повторном создании).
          id (Column): ID пользователя (первичный ключ).
          username (Column): Имя пользователя.
          firstname (Column): Имя пользователя.
          lastname (Column): Фамилия пользователя.
          age (Column): Возраст пользователя.
          email (Column): Email пользователя.
          slug (Column): Уникальный слаг пользователя (для URL).
          tasks (relationship): Связь с моделью Task (one-to-many)."""
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    email = Column(String)
    slug = Column(String, unique=True, index=True)

    tasks = relationship("Task", back_populates="user")


from sqlalchemy.schema import CreateTable

print(CreateTable(User.__table__))
