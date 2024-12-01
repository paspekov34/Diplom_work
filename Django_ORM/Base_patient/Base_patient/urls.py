"""
URL configuration for Base_patient project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task.views import Main_page_cl, menu_def, main_page_def, register, registration_complete, menu_def_2
"""
    URL-шаблоны для приложения.

    Назначает URL-адреса для различных представлений:
    - admin/: Админ-панель Django.
    - '': Главная страница (Main_page_cl).
    - main_page/nutrio/: Страница с продуктами нутрициологии (menu_def_2).
    - main_page/cardio/: Страница с продуктами кардиологии (menu_def).
    - main_page/: Главная страница (main_page_def).
    - main_page/registration_page/: Страница регистрации (register).
    - main_page/registration_compl/: Страница подтверждения регистрации (registration_complete).
    """
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main_page_cl.as_view()),
    path('main_page/nutrio/', menu_def_2),
    path('main_page/cardio/', menu_def),
    path('main_page/', main_page_def, name='main_page'),
    path('main_page/registration_page/', register),
    path('main_page/registration_compl/', registration_complete, name='registration_compl')
]
