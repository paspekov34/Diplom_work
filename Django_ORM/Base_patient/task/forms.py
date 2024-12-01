from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Patient


class UserRegister(UserCreationForm):
    """
        Форма регистрации пользователя.  Расширяет UserCreationForm для добавления дополнительных полей.

        Добавлены поля для имени, фамилии, email и возраста.  Пароль обрабатывается UserCreationForm.
        После успешного сохранения формы создается объект Patient, связанный с созданным пользователем.

        Attributes:
            first_name (CharField): Фамилия пользователя.
            last_name (CharField): Имя пользователя.
            email (EmailField): Email пользователя.
            age (IntegerField): Возраст пользователя.
        """
    first_name = forms.CharField(max_length=10, label='Фамилия')
    last_name = forms.CharField(max_length=10, label='Имя')
    email = forms.EmailField(max_length=254, label='Электронная почта')
    age = forms.IntegerField(label='Введите свой возраст', min_value=18, max_value=110)

    class Meta(UserCreationForm.Meta):
        """Мета-класс, определяющий поля формы."""
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'age')

    def save(self, commit=True):
        """
               Сохраняет форму.  Создает пользователя и связанного с ним пациента.
               Args:
                   commit (bool): Флаг, указывающий, нужно ли сразу сохранять данные в базу данных.
               Returns:
                   User: Объект созданного пользователя.
               """
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.save()
        patient = Patient(user=user, first_name=self.cleaned_data['first_name'],
                          last_name=self.cleaned_data['last_name'], age=self.cleaned_data['age'],
                          email=self.cleaned_data['email'])
        patient.save()
        return user
