from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Patient(models.Model):
    """
        Модель пациента.  Содержит информацию о пациенте, связанную с пользователем Django.

        Attributes:
            user (ForeignKey): Связь с моделью пользователя Django (User).  Удаление пользователя приводит к удалению пациента.
            first_name (CharField): Имя пациента.
            last_name (CharField): Фамилия пациента.
            age (IntegerField): Возраст пациента.
            email (EmailField): Email пациента (уникальный).
        """
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    age = models.IntegerField()
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        """Возвращает строковое представление объекта Patient."""
        return f"{self.last_name}, {self.first_name}"


class Product(models.Model):
    """
        Модель продукта (годовое сопровождение).

        Attributes:
            patient (ForeignKey): Связь с моделью Patient. Может быть пустым.
            title (CharField): Название продукта.
            cost (DecimalField): Стоимость продукта.
            problem_description (TextField): Описание проблемы.
            age_limited (BooleanField): Признак ограничения по возрасту.
            created_at (DateTimeField): Дата и время создания продукта (автоматически заполняется).
            edited_at (DateTimeField): Дата и время последнего редактирования продукта (автоматически заполняется).
        """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,
                                related_name='products_patient', blank=True, null=True)
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=1000000, decimal_places=2)
    problem_description = models.TextField()
    age_limited = models.BooleanField(default=False)
    created_at = models.DateTimeField('дата и время создания продукта', auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Годовое сопровождение'
        verbose_name_plural = 'Годовое сопровождение'
        ordering = ['-created_at']

    def __str__(self):
        """Возвращает строковое представление объекта Product."""
        return f"{self.title}, {self.cost}"


class Product2(models.Model):
    """
       Модель продукта (марафон похудения).  Аналогична модели Product.

       Attributes:
           patient (ForeignKey): Связь с моделью Patient. Может быть пустым.
           title (CharField): Название продукта.
           cost (DecimalField): Стоимость продукта.
           problem_description (TextField): Описание проблемы.
           age_limited (BooleanField): Признак ограничения по возрасту.
           created_at (DateTimeField): Дата и время создания продукта (автоматически заполняется).
           edited_at (DateTimeField): Дата и время последнего редактирования продукта (автоматически заполняется).
       """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,
                                related_name='products_patient2', blank=True, null=True)
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=1000000, decimal_places=2)
    problem_description = models.TextField()
    age_limited = models.BooleanField(default=False)
    created_at = models.DateTimeField('дата и время создания продукта', auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Марафон похудения'
        verbose_name_plural = 'Марафон похудения'
        ordering = ['-created_at']

    def __str__(self):
        """Возвращает строковое представление объекта Product2."""
        return f"{self.title}, {self.cost}"
