📚 Сравнение производительности и удобства использования различных ORM
(Object-Relational Mapping) библиотек: Django ORM, SQLAlchemy и Tortoise
ORM Это простые веб-приложения для создания пользователей, задач, и
продуктов, онлайн ведения врача кардиолога-нутрициолога с использованием
базы данных SQLite.

🚀 Установка приложений: Django_ORM Клонируйте репозиторий:

https://github.com/paspekov34/Diplom_work Перейдите в папку проекта,
написав в консоли:

cd Django_ORM сd Base_patient Установите необходимые библиотеки: pip install django

Запустите приложение: python manage.py runserver 

Django ORM - это часть фреймворка Django. Он тесно интегрирован с другими компонентами Django, что делает разработку веб-приложений внутри Django очень удобной и согласованной. Предоставляет очень высокоуровневый интерфейс для взаимодействия с базой данных. Он скрывает большинство деталей SQL. Из-за высокой степени абстракции Django ORM может быть менее гибким, чем SQLAlchemy, когда дело доходит до выполнения сложных запросов или работы с нестандартными базами данных. Предоставляет мощную систему миграций для управления изменениями схемы базы данных.

Добавьте в конец в адресной строки /admin, переход в админ панель. логин: test, пароль: 1234

После чего вы переидете на страницу управления где можно добавлять, удалять пользователей и задачи.

![Админка 1](https://github.com/user-attachments/assets/3de6aefc-9605-46b5-8361-ae51a3f0cef5)

![админка2](https://github.com/user-attachments/assets/b48aa562-c96a-41c1-884b-ea7c77e4d8b7)

![админка 3](https://github.com/user-attachments/assets/1abda356-385e-4ac1-a113-82b5fa7a8ac3)

Также имеется "Главная страница" где можно выбрать в категориях "Кардиология и Нутрициология выбрать продукт. А также зарегистрироваться.

![Главная](https://github.com/user-attachments/assets/b6e52568-bfa2-47c9-a82c-495a46553009)

![Кардиоглогия](https://github.com/user-attachments/assets/ad5235a9-6996-4546-81c7-214801b4a2b4)

![Нутрипродукты](https://github.com/user-attachments/assets/f1b7e56a-7da2-457c-ab88-542decbd7801)

![Регистрация](https://github.com/user-attachments/assets/09c2c359-155a-4895-a7ed-e830644ff4ba)

При неправильной регистрации выдает ошибку например "Пользователь с таким "email" ужу существует.

![Ошибка рег](https://github.com/user-attachments/assets/e931f2ad-e9fb-49bb-9681-fe91add0a7c0)

Если регистрация проходит успешно переходит на страницу с соответсвующим сообщением и кнопкой возврата на главную страницу.

![Успешная рег](https://github.com/user-attachments/assets/5baa31bc-2032-4169-ab92-83beebcc8b70)

Все пользователи и задачи добавляются в таблицу.

![Таблица](https://github.com/user-attachments/assets/b6e33b23-96e1-47a4-ac98-c34c562cdcdc)



SQLAlchemy_ORM Используйте тот же репозиторий:

Перейдите в папку проекта, написав в консоли: cd SQLAlchemy_ORM, cd app 

Установите необходимые бибилиотеки: pip install sqlalchemy pip install fastapi pip install uvicorn pip
install alembic pip install pydantic 

Запустите приложение: uvicorn main:app

SQLAlchemy отличается от Джанго независимой библиотекой которая не привязана к какому-либо веб-фреймворку, имеет высокий уровень гибкости, больший контроль над SQL что позволяет оптимизировать запросы. Но имеет более высокую сложность.

Простое приложение для управления пользователями и задачами. Где можно их добавить, изменить, удалить по id. Вывести всех пользователей и все задачи.

![Главная](https://github.com/user-attachments/assets/b0b42db0-50e8-4189-98ac-c0fa9f9c0b67)

![Главная 2](https://github.com/user-attachments/assets/6af93788-1a59-494a-8a90-c8cc4da1fcee)

![Главная 3](https://github.com/user-attachments/assets/c272a602-ffff-462e-acde-79f4a4ae695a)


Создание пользователя и создание его данных в таблице

![Создание юзера](https://github.com/user-attachments/assets/797c6ce8-6e7d-4448-aa9e-dbb93ec8b1c8)

![Успешное созд юзера](https://github.com/user-attachments/assets/ae291697-e846-4f99-956f-fc439d071cb2)

![таблица создание](https://github.com/user-attachments/assets/6bf6316d-8681-4e86-a1bc-cfb596d4e6bf)

Изменение пользователя и изменение данных в таблице.

![изменение юзера](https://github.com/user-attachments/assets/5741db5f-018d-466f-a3f2-5bc9ed165c3d)

![Изменение юзера таблица](https://github.com/user-attachments/assets/0963f307-4888-4618-a981-82f1552c58a8)

Удаление пользователя и его данных из таблицы.

![Удаление юзера](https://github.com/user-attachments/assets/f6ffa349-772a-4a4b-960c-118e1144c0a8)

![удаление юзера таблица](https://github.com/user-attachments/assets/cb4b8aa1-144b-41aa-8c67-0a77180e5a72)


Такие же действия можно сделать с задачами а так же взаимодействия по id пользователя.

![Создание задачи](https://github.com/user-attachments/assets/d889c7a8-eae4-43a5-9f58-63b28046c84b)

![создание задачи таблица](https://github.com/user-attachments/assets/dd12ccdd-22a8-4398-95a5-8305451fc926)


Изменение.

![Изменение задачи](https://github.com/user-attachments/assets/a434c55a-336f-4dff-8d7b-e5ebe3bc1bbb)

![изменение задачи таблица](https://github.com/user-attachments/assets/c755d1f3-6f97-4cd6-9ea7-6ffa7eb4a4a0)


Удаление.

![Удаление задачи](https://github.com/user-attachments/assets/ecd8342d-bed3-438d-83bf-2fe66e00fc0b)

![Удаление задачи таблица](https://github.com/user-attachments/assets/4dfded5a-9ced-4e50-835c-721f20144d77)


Tortoise_ORM Используйте тот же репозиторий:

Перейдите в папку проекта, написав в консоли: cd Tortoise_ORM 
Установите необходимые бибилиотеки: pip install tortoise aiosqlite pydantic

Переход к веб-приложению осуществляется командой в терминале: uvicorn manage_product:app

Работа с базой данных: Приложение идентично с SQLAlchemy приложением так как используется тот же веб-фреймворк "FastAPI".
Однако есть отличия отсутствует таблица задач в приложении. В написании кода, так как используются разные "ORM". "Tortoise" полностью асинхронный, доступ к данным ипользует методы ORM а у SQLAlchemy  доступ прямой через Session. Генерация DTO в "Черепахе" автоматическая через pydantic_model_creator, у "Алхимии" же вручную. 

Приложение имеет только таблицу пользователей так же есть приветсвенная запись при переходе по ссылке.

![Приветсвенная](https://github.com/user-attachments/assets/a4a0d893-79cc-4d60-bdcb-492e711e6bf5)

Методы добавления пользователей.

![Создание юзера](https://github.com/user-attachments/assets/2cc465fb-1d61-434d-83ba-02c40eb36372)

Вывод всех пользователей.

![вывод всех юзеров](https://github.com/user-attachments/assets/8ccc828a-9c02-4e78-8a96-4d2184e2db5e)

Изменение.

![изменение1](https://github.com/user-attachments/assets/34fbb0fb-83ef-4205-b756-26b3d5d11b27)

![изменение 2](https://github.com/user-attachments/assets/f358305c-2ea4-4de5-90a0-ee686db2a425)

Удаление

![Удаление 1](https://github.com/user-attachments/assets/bc4b665b-987d-43d2-9dff-4ad2cfef6cac)

![удаление 2](https://github.com/user-attachments/assets/cba74b3b-8e05-485f-a8aa-c47bb400c45e)



👨‍💻 Спасибо за внимание!
