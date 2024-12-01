from tortoise import Tortoise
from user.models import User
from tortoise.contrib.pydantic import pydantic_model_creator
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI(title="Tortoise ORM с FastAPI")


async def connect_db():
    """
        Подключается к базе данных и генерирует схему.
        """
    await Tortoise.init(
        db_url="sqlite://product.db",
        modules={"models": ["user.models", "task.models"]})
    await Tortoise.generate_schemas()


User_Pydantic = pydantic_model_creator(User, name="User")
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)
UserUpdate_Pydantic = pydantic_model_creator(User, name="UserUpdate",
                                             exclude_readonly=True, exclude={"user_id"})


@app.on_event("startup")
async def startup_event():
    """
       Подключается к базе данных при запуске приложения.
       """
    await connect_db()


@app.on_event("shutdown")
async def shutdown_event():
    """
        Закрывает соединения с базой данных при завершении работы приложения.
        """
    await Tortoise.close_connections()


@app.get('/')
async def welcome():
    """
        Приветственная страница API.
        Returns:
            dict: Словарь с приветственным сообщением.
        """
    return {'message': "Добро пожаловать в менеджер!"}


@app.post("/users/", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    """
        Создает нового пользователя.
        Args:
            user: Данные пользователя для создания.
        Returns:
            Созданный пользователь.
        """
    user_obj = await User.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)


@app.put("/users/{user_id}", response_model=User_Pydantic)
async def update_user(user_id: int, user: UserUpdate_Pydantic):
    """Обновляет данные пользователя по ID.
    Args:
        user_id: ID пользователя для обновления.
        user: Данные для обновления.
    Returns:
        Обновленный пользователь.
    Raises:
        HTTPException: Если пользователь не найден.
    """
    try:
        user_obj = await User.get(user_id=user_id)
        await user_obj.update_from_dict(user.dict(exclude_unset=True))
        await user_obj.save()
        return await User_Pydantic.from_tortoise_orm(user_obj)
    except User.DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")


@app.get("/users/", response_model=list[User_Pydantic])
async def get_users():
    """
        Получает всех пользователей.
        Returns:
            Список всех пользователей.
        """
    return await User_Pydantic.from_queryset(User.all())


@app.get("/users/{user_id}", response_model=User_Pydantic)
async def get_user(user_id: int):
    """
        Получает пользователя по ID.
        Args:
            user_id: ID пользователя для получения.
        Returns:
            Пользователь с заданным ID.
        Raises:
            HTTPException: Если пользователь не найден.
        """
    user = await User.get(user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return await User_Pydantic.from_tortoise_orm(user)


@app.delete("/users/{user_id}", status_code=204)
async def delete_user(user_id: int):
    """
       Удаляет пользователя по ID.
       Args:
           user_id: ID пользователя для удаления.
       Raises:
           HTTPException: Если пользователь не найден или ID неверен.
           HTTPException: Если произошла ошибка базы данных.
       """
    try:
        user_id = int(user_id)
        user = await User.get(user_id=user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        await user.delete()
    except ValueError:
        raise HTTPException(status_code=422, detail="Invalid user ID")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
