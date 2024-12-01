from backend.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class Task(Base):
    """
        Представляет задачу в базе данных.
        Атрибуты:
            id (int): Уникальный идентификатор задачи.
            title (str): Заголовок задачи.
            content (str): Содержание или описание задачи.
            priority (int): Уровень приоритета задачи (более высокое значение означает более высокий приоритет). По умолчанию 0.
            completed (bool): Поле, указывающее, завершена ли задача. По умолчанию False.
            user_id (int): ID пользователя, которому принадлежит задача. Внешний ключ, ссылающийся на таблицу `users`.
            slug (str): Уникальный URL-дружественный идентификатор задачи.
            user: Отношение SQLAlchemy к модели User, предоставляющее доступ к объекту пользователя, связанному с задачей.

        """
    __tablename__ = "tasks"
    __table_args__ = {"keep_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)

    user = relationship("User", back_populates="tasks")


from sqlalchemy.schema import CreateTable

print(CreateTable(Task.__table__))
