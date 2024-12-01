from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("sqlite:///patient_manager.db", echo=True)
"""
Создает движок SQLAlchemy для базы данных SQLite.
Args:
    "sqlite:///patient_manager.db": URL подключения к базе данных.  Файл базы данных будет создан, если он не существует.
    echo=True: Включает вывод SQL-запросов в консоль (полезно для отладки).
"""

SessionLocal = sessionmaker(bind=engine)
"""
Создает локальный генератор сессий SQLAlchemy.
Args:
    bind=engine:  Привязывает генератор сессий к созданному движку базы данных.
"""


class Base(DeclarativeBase):
    """
        Базовый класс для всех моделей SQLAlchemy.  Используется для автоматического создания таблиц в базе данных.
        """
    pass
