from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path(
        'about/',
        views.AboutView.as_view(),
        name='about'
    ),
    path(
        'intro/',
        views.IntroView.as_view(),
        name='intro'
    ),
    path(
        'ending/',
        views.EndingView.as_view(),
        name='ending'
    ),
    path(
        'glossary/',
        views.GlossaryView.as_view(),
        name='glossary'
    ),
    path(
        'library/',
        views.LibrarytView.as_view(),
        name='library'
    ),
]
