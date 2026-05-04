"""
URL-маршрутизация приложения 'students_book'.
Определяет пути к конкретным параграфам учебника.
"""

from django.urls import path

from . import views

app_name = 'students_book'

urlpatterns = [
    # Маршрут для просмотра параграфа по его уникальному идентификатору (ID)
    path('paragraph/<int:paragraph_id>/', views.paragraph_detail, name='paragraph_detail'),
]