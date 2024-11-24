from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    age = models.IntegerField()
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Product(models.Model):
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
        return f"{self.title}, {self.cost}"


class Product2(models.Model):
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
        return f"{self.title}, {self.cost}"
