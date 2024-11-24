from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import UserRegister
from .models import Patient, Product, Product2
from django.contrib.auth.models import User
from django.db import IntegrityError


class Main_page_cl(TemplateView):
    template_name = 'main_page.html'


def main_page_def(request):
    return render(request, 'main_page.html')


def menu_def(request):
    products = Product.objects.all()
    context = {'mydict': products}
    return render(request, 'cardio.html', context)


def menu_def_2(request):
    products_nutrio = Product2.objects.all()
    context = {'mydict2': products_nutrio}
    return render(request, 'nutrio.html', context)


def register(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            age = form.cleaned_data['age']

            if User.objects.filter(username=username).exists() or Patient.objects.filter(email=email).exists():
                return render(request, 'registration_page.html',
                              {'form': form, 'error': 'Пользователь с таким именем или email уже существует'})

            try:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=first_name, last_name=last_name)
                Patient.objects.create(user=user, age=age, email=email)
                return redirect('registration_compl')
            except IntegrityError:
                return render(request, 'registration_page.html',
                              {'form': form, 'error': 'Ошибка создания пользователя'})
            except Exception as e:
                return render(request, 'registration_page.html', {'form': form, 'error': str(e)})
        else:  # Обработка form.is_valid() == False
            return render(request, 'registration_page.html',
                          {'form': form, 'error': 'Ошибка в форме'})  # или более конкретные сообщения об ошибках

    else:
        form = UserRegister()
        return render(request, 'registration_page.html', {'form': form})


def registration_complete(request):
    return render(request, 'registration_compl.html')
