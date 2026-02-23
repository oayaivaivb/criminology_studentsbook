from django.views.generic import TemplateView
from django.shortcuts import render


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class IntroView(TemplateView):
    template_name = 'pages/intro.html'


class EndingView(TemplateView):
    template_name = 'pages/ending.html'


class GlossaryView(TemplateView):
    template_name = 'pages/glossary.html'


class LibrarytView(TemplateView):
    template_name = 'pages/library.html'