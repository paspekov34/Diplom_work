📚 Сравнение производительности и удобства использования различных ORM
(Object-Relational Mapping) библиотек: Django ORM, SQLAlchemy и Tortoise
ORM Это простые веб-приложения для создания пользователей, задач, и
продуктов онлайн ведения врача кардиолога-нутрициолога с использованием
базы данных SQLite.

🚀 Установка приложений: Django_ORM Клонируйте репозиторий:

https://github.com/paspekov34/Diplom_work Перейдите в папку проекта,
написав в консоли:

cd Django_ORM сd Base_patient Установите необходимые библиотеки:

pip install django

Запустите приложение:

python manage.py runserver 

Введите в адресной строке /admin, переход в админ панель. логин: test, пароль: 1234

SQLAlchemy_ORM Используйте тот же
репозиторий:

Перейдите в папку проекта, написав в консоли:

cd SQLAlchemy_ORM Установите необходимые бибилиотеки:

pip install sqlalchemy pip install fastapi pip install uvicorn pip
install alembic pip install pydantic Запустите приложение:

python -m app.main

Tortoise_ORM Используйте тот же репозиторий:

Перейдите в папку проекта, написав в консоли:

cd Tortoise_ORM Установите необходимые бибилиотеки:

pip install tortoise pip install tortoise-orm Работа с базой данных:
Переидите в файл manage_product: Где можно добавлять удалять продукты из
базы разкоментировав #run_async(create_product())
#run_async(query_product()) #run_async(update_product())
run_async(delete_product()) #run_async(create_user())
#run_async(create_task()) для добавления и удаления вызвать в консоли:
python manage_product.py

💡 Использование Django_ORM В приложении можно зарегистрироваться
выбрать продукт, из 2 категорий



SQLAlchemy_ORM и Tortoise_ORM Добавив в адресной строке /docs вы
попадаете на страницу Swagger:

👨‍💻 Спасибо за внимание!