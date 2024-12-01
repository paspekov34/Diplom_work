from tortoise import fields, models
from tortoise.models import Model


class User(models.Model):
    """
        Модель пользователя в базе данных.
        Attributes:
            user_id (IntField): Уникальный идентификатор пользователя (первичный ключ).
            username (CharField): Имя пользователя (строка, макс. 250 символов).
            firstname (CharField): Имя пользователя (строка, макс. 250 символов).
            lastname (CharField): Фамилия пользователя (строка, макс. 250 символов).
            age (IntField): Возраст пользователя (целое число, по умолчанию 0).
        """
    user_id = fields.IntField(pk=True, index=True)
    username = fields.CharField(max_length=250)
    firstname = fields.CharField(max_length=250)
    lastname = fields.CharField(max_length=250)
    age = fields.IntField(default=0)

    def __str__(self):
        """
            Возвращает строковое представление модели пользователя.
                """
        return self.username
