"""
Представления (views) приложения 'pages'.
Отвечают за отображение статических информационных страниц сайта.
"""

from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class IntroView(TemplateView):
    template_name = 'pages/intro.html'

class EndingView(TemplateView):
    template_name = 'pages/ending.html'

class GlossaryView(TemplateView):
    template_name = 'pages/glossary.html'

class LibraryView(TemplateView):
    template_name = 'pages/library.html'