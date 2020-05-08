"""
Пример программы для работы с условиями
"""

original_password = "test"
user_password = input("Введите пароль >> ")

if original_password == user_password:
    print("OK")
else:
    print("Fail")