from pydantic import BaseModel


class CreateUser(BaseModel):
    """
        Схема для создания нового пользователя.
        Attributes:
            username (str): Имя пользователя.
            firstname (str): Имя.
            lastname (str): Фамилия.
            email (str): Email адрес.
            age (int): Возраст.
        """
    username: str
    firstname: str
    lastname: str
    email: str
    age: int


class UpdateUser(BaseModel):
    """
        Схема для обновления данных пользователя.
        Attributes:
            username (str): Имя пользователя.
            firstname (str): Имя.
            lastname (str): Фамилия.
            email (str): Email адрес.
            age (int): Возраст.
        Note:
            Все поля являются необязательными.  Если поле не указано, оно не будет изменено.
        """
    username: str
    firstname: str
    lastname: str
    email: str
    age: int


class CreateTask(BaseModel):
    """
        Схема для создания новой задачи.
        Attributes:
            title (str): Заголовок задачи.
            content (str): Содержание задачи.
            priority (int): Приоритет задачи (целое число).
        """
    title: str
    content: str
    priority: int


class UpdateTask(BaseModel):
    """
        Схема для обновления данных задачи.
        Attributes:
            title (str): Заголовок задачи.
            content (str): Содержание задачи.
            priority (int): Приоритет задачи (целое число).
        Note:
            Все поля являются необязательными.  Если поле не указано, оно не будет изменено.
        """
    title: str
    content: str
    priority: int

