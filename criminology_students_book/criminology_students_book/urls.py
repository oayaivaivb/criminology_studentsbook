from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='pages:about', permanent=True)),
    path('students_book/', include('students_book.urls')),
    path('pages/', include('pages.urls')),
]
