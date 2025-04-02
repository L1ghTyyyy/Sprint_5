import random
import string

# Генератор логинов
def generate_login(domain="yandex.ru"):
    """Генерирует случайный логин в формате имя_фамилия_номер_когорты_любые_3_цифры@домен"""
    return f"andreybobylev20{random.randint(100, 999)}@{domain}"

# Генератор паролей
def generate_password(length=8):
    """Генерирует случайный пароль длиной length."""
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"  # Допустимые символы
    return "".join(random.choices(characters, k=length))
