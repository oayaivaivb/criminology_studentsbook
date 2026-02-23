from django.urls import path

from . import views

app_name = 'students_book'

urlpatterns = [
    path(
        'paragraph/<int:paragraph_id>/',
        views.paragraph_detail,
        name='paragraph_detail'
    ),
]
