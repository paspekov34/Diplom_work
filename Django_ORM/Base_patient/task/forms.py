from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    first_name = forms.CharField(max_length=10, label='Фамилия')
    last_name = forms.CharField(max_length=10, label='Имя')
    email = forms.EmailField(max_length=254, label='Электронная почта')
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, label='Введите пароль')
    repeat_password = forms.CharField(widget=forms.PasswordInput(), min_length=8, label='Повторите пароль')
    age = forms.IntegerField(label='Введите свой возраст', min_value=18, max_value=110)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")

        if password != repeat_password:
            raise forms.ValidationError("Пароли не совпадают")
        return cleaned_data
