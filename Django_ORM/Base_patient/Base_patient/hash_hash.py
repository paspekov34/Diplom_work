from django.contrib.auth.hashers import make_password

"""
Пример использования функции make_password для хеширования пароля.

Функция make_password() из модуля django.contrib.auth.hashers используется для безопасного хеширования паролей 
перед их сохранением в базе данных.  Она использует алгоритм PBKDF2_SHA256 по умолчанию, что обеспечивает 
высокую защиту от атак методом грубой силы.

"""
hash_pass = make_password('1234P')
print(hash_pass)
