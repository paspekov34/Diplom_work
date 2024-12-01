from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.exc import SQLAlchemyError
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from models.user import User
from models.task import Task
from schemas import CreateUser, UpdateUser
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    """
        Возвращает всех пользователей из базы данных.
        Args:
            db (Session): Объект сессии SQLAlchemy.
        Returns:
            list: Список всех пользователей.
        """
    users = db.scalars(select(User)).all()
    return users


@router.get("/user_id")
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    """
        Возвращает пользователя по ID.
        Args:
            db (Session): Объект сессии SQLAlchemy.
            user_id (int): ID пользователя.
        Returns:
            User: Пользователь с заданным ID.
        Raises:
            HTTPException: Если пользователь не найден (404).
        """

    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пользователь не найден'
        )
    return user

@router.get("/user_id/tasks")
def tasks_by_user_id(db: Annotated[Session, Depends(get_db)], user_id: int):
  try:
    user = db.query(User).get(user_id)
    if user is None:
      raise HTTPException(status_code=404, detail="Пользователь не найден")

    tasks = db.scalars(select(Task).where(Task.user_id == user_id)).all()
    return tasks
  except SQLAlchemyError as e:
    raise HTTPException(status_code=500, detail=f"Ошибка базы данных: {e}")
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Внутренняя ошибка сервера: {e}")


@router.post("/create")
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    """
        Создает нового пользователя.
        Args:
            db (Session): Объект сессии SQLAlchemy.
            create_user (CreateUser): Данные для создания пользователя (Pydantic schema).
        Returns:
            dict: Сообщение об успешном создании пользователя.
        """
    db.execute(insert(User).values(username=create_user.username,
                                   firstname=create_user.firstname,
                                   lastname=create_user.lastname,
                                   age=create_user.age,
                                   email=create_user.email,
                                   slug=slugify(create_user.username)))

    db.commit()

    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Успешное добавление пользователя'
    }



@router.put("/update")
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_user: UpdateUser):
    """
       Обновляет данные существующего пользователя.
       Args:
           db (Session): Объект сессии SQLAlchemy.
           user_id (int): ID пользователя для обновления.
           update_user (UpdateUser): Данные для обновления пользователя (Pydantic schema).
       Raises:
           HTTPException: 404, если пользователь не найден.
       """
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пользователь не найден'
        )

    db.execute(update(User).where(User.id == user_id).values(username=update_user.username,
                                                             firstname=update_user.firstname,
                                                             lastname=update_user.lastname,
                                                             age=update_user.age,
                                                             email=update_user.email))
    db.commit()


@router.delete("/delete")
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    """
        Удаляет пользователя по ID.
        Args:
            db (Session): Объект сессии SQLAlchemy.
            user_id (int): ID пользователя для удаления.
        Returns:
            dict: Сообщение об успешном удалении пользователя.
        Raises:
            HTTPException: 404, если пользователь не найден.
        """
    user = db.scalars(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пользователь не найден'
        )

    db.execute(delete(User).where(User.id == user_id))
    db.commit()

    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Удаление пользователя завершилось успешно'
    }


@router.get("/user_id/tasks")
def tasks_by_user_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    tasks = db.scalars(select(Task).where(Task.user_id == user_id)).all()

    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }
