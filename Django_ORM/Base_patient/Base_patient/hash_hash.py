from django.contrib.auth.hashers import make_password

hash_pass = make_password('1234P')
print(hash_pass)