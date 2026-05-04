"""
Конфигурация приложения 'pages'.
"""

from django.apps import AppConfig


class PagesConfig(AppConfig):
    # Указываем тип поля для первичного ключа по умолчанию
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Название приложения
    name = 'pages'