from fastapi import FastAPI
from routers import task, user

app = FastAPI()


@app.get('/')
async def welcome():
    """
        Приветственная страница API.
        Returns:
            dict: Словарь с приветственным сообщением.
        """
    return {'message': "Добро пожаловать в менеджер 'Сердечно с Татьяной Дворцовой'"}


app.include_router(task.router)
app.include_router(user.router)