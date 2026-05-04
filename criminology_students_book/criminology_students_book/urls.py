"""
Criminology Students Book - Главный маршрутизатор проекта.
Этот файл определяет иерархию URL-адресов и перенаправляет запросы к 
соответствующим приложениям.
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # Интерфейс администратора
    path('admin/', admin.site.urls),

    # Главная страница: редирект на раздел 'about' в приложении 'pages'
    # permanent=True сообщает браузерам и поисковикам, что это постоянный адрес
    path('', RedirectView.as_view(pattern_name='pages:about', permanent=True)),

    # Подключение маршрутов приложений (модульная архитектура)
    path('students_book/', include('students_book.urls')),
    path('pages/', include('pages.urls')),
]