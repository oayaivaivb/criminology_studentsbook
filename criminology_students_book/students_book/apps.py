"""
Конфигурация приложения 'students_book'.
"""

from django.apps import AppConfig


class StudentsBookConfig(AppConfig):
    # Указываем тип поля для первичного ключа по умолчанию
    default_auto_field = 'django.db.models.BigAutoField'

    # Название приложения
    name = 'students_book'