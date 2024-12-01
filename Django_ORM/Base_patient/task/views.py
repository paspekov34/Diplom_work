from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import UserRegister
from .models import Patient, Product, Product2
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages


class Main_page_cl(TemplateView):
    """
       Представление для главной страницы. Использует шаблон 'main_page.html'.
       """
    template_name = 'main_page.html'


def main_page_def(request):
    """
        Функция-представление для главной страницы. Рендерит шаблон 'main_page.html'.
        """
    return render(request, 'main_page.html')


def menu_def(request):
    """
      Функция-представление для страницы с продуктами (кардио).
      Получает все продукты из модели Product и передает их в контекст.
      Рендерит шаблон 'cardio.html'.
      """
    products = Product.objects.all()
    context = {'mydict': products}
    return render(request, 'cardio.html', context)


def menu_def_2(request):
    """
      Функция-представление для страницы с продуктами (нутрициология).
      Получает все продукты из модели Product2 и передает их в контекст.
      Рендерит шаблон 'nutrio.html'.
      """
    products_nutrio = Product2.objects.all()
    context = {'mydict2': products_nutrio}
    return render(request, 'nutrio.html', context)


def register(request):
    """
       Функция-представление для страницы регистрации.
       Обрабатывает POST-запросы для регистрации нового пользователя и создания связанного с ним пациента.
       В случае успеха перенаправляет на страницу успешной регистрации.
       В случае ошибки отображает форму с сообщением об ошибке.
       """
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            try:
                user = form.save()  # UserCreationForm сам обрабатывает пароль и создание пользователя
                patient = Patient.objects.create(user=user, age=form.cleaned_data['age'])
                messages.success(request, 'Регистрация прошла успешно!')
                return redirect('registration_compl')
            except IntegrityError:
                messages.error(request, 'Ошибка создания пользователя. Возможно, такой email уже существует.')
            except Exception as e:
                messages.error(request, f'Произошла непредвиденная ошибка: {e}')
        else:  # Обработка form.is_valid() == False
            messages.error(request, 'Ошибка в форме. Проверьте правильность заполнения полей.')
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form})


def registration_complete(request):
    """
    Функция-представление для страницы подтверждения регистрации.  Отображает сообщение об успехе
    или ошибку, если передано в параметрах запроса.
    """
    message = request.GET.get('message') #получаем сообщение из GET параметров
    context = {'message': message}
    return render(request, 'registration_compl.html', context)
