from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import insert, select, update, delete
from sqlalchemy.exc import SQLAlchemyError

from typing import Annotated
from slugify import slugify

from backend.db_depends import get_db
from models.task import Task
from models.user import User
from schemas import CreateTask, UpdateTask

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
  """
   Получает все задачи из базы данных.
   Args:
     db (Session): Объект сессии SQLAlchemy.
   Returns:
     list: Список всех задач.
   """
  tasks = db.scalars(select(Task)).all()
  return tasks


@router.get("/task_id")
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
  """
   Получает задачу по ID.
   Args:
     db (Session): Объект сессии SQLAlchemy.
     task_id (int): ID задачи.
   Returns:
     Task: Задача с заданным ID.
   Raises:
     HTTPException: Если задача не найдена (404).
   """
  task = db.scalars(select(Task).where(Task.id == task_id)).first()
  if task is None:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, detail="Задача не найдена"
    )
  return task


@router.post("/create")
async def create_task(
    db: Annotated[Session, Depends(get_db)], create_task: CreateTask, user_id: int
):
  """
    Создает новую задачу.
    Args:
      db (Session): Объект сессии SQLAlchemy.
      create_task (CreateTask): Данные для создания задачи (Pydantic schema).
      user_id (int): ID пользователя, которому принадлежит задача.
    Returns:
      dict: Сообщение об успешном создании задачи.
    Raises:
      HTTPException:
        - 404: Если пользователь не найден.
        - 500: При ошибке базы данных или внутренней ошибке сервера.
    """
  try:
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if user is None:
      raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Пользователь не найден"
      )
    db.execute(
      insert(Task).values(
        title=create_task.title,
        content=create_task.content, # Исправленное сопоставление полей
        priority=create_task.priority, # Исправленное сопоставление полей
        user_id=user_id,
        slug=slugify(create_task.title),
      )
    )
    db.commit()
    return {"status": status.HTTP_201_CREATED, "transaction": "Успешно"}
  except SQLAlchemyError as e:
    db.rollback()
    raise HTTPException(status_code=500, detail=f"Ошибка базы данных: {e}")
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Внутренняя ошибка сервера: {e}")



@router.put("/update")
async def update_task(
    db: Annotated[Session, Depends(get_db)], update_task: UpdateTask, task_id: int,
):
  """
    Обновляет существующую задачу.
    Args:
      db (Session): Объект сессии SQLAlchemy.
      update_task (UpdateTask): Данные для обновления задачи (Pydantic schema).
      task_id (int): ID задачи для обновления.
    Returns:
      dict: Сообщение об успешном обновлении задачи.
    Raises:
      HTTPException:
        - 404: Если задача не найдена.
        - 500: При ошибке базы данных или внутренней ошибке сервера.
    """
  try:
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if task is None:
      raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Задача не найдена"
      )
    db.execute(
      update(Task)
      .where(Task.id == task_id)
      .values(
        title=update_task.title, # Исправленная схема
        content=update_task.content, # Исправленная схема
        priority=update_task.priority, # Исправленная схема
        slug=slugify(update_task.title),
      )
    )
    db.commit()
    return {"status": status.HTTP_200_OK, "transaction": "Успешно"}
  except SQLAlchemyError as e:
    db.rollback()
    raise HTTPException(status_code=500, detail=f"Ошибка базы данных: {e}")
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Внутренняя ошибка сервера: {e}")


@router.delete("/delete")
async def delete_tasks(db: Annotated[Session, Depends(get_db)], task_id: int):
  """
    Удаляет задачу по ID.
    Args:
      db (Session): Объект сессии SQLAlchemy.
      task_id (int): ID задачи для удаления.
    Returns:
      dict: Сообщение об успешном удалении задачи.
    Raises:
      HTTPException:
        - 404: Если задача не найдена.
        - 500: При ошибке базы данных или внутренней ошибке сервера.
    """
  try:
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if task is None:
      raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Задача не найдена"
      )
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {
      "status_code": status.HTTP_200_OK,
      "transaction": "Удаление задачи успешно завершено",
    }
  except SQLAlchemyError as e:
    db.rollback()
    raise HTTPException(status_code=500, detail=f"Ошибка базы данных: {e}")
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Внутренняя ошибка сервера: {e}")