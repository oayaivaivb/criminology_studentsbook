"""
Представления (views) приложения 'students_book'.
Обеспечивают отображение страниц учебника на основе статического словаря.
"""

from django.http import Http404
from django.shortcuts import render

# Конфигурация глав: ID -> {заголовок, путь к шаблону}
PARAGRAPHS = {
    1: {'title': 'Понятие криминологии как науки, ее предмет, задачи, функции', 'template': 'students_book/paragraph1.html'},
    2: {'title': 'Преступность как социальное явление', 'template': 'students_book/paragraph2.html'},
    3: {'title': 'Личность преступника', 'template': 'students_book/paragraph3.html'},
    4: {'title': 'Причины и условия преступности', 'template': 'students_book/paragraph4.html'},
    5: {'title': 'Предупреждение преступности', 'template': 'students_book/paragraph5.html'},
    6: {'title': 'Методика криминологических исследований', 'template': 'students_book/paragraph6.html'},
    7: {'title': 'Криминологическая характеристика отдельных видов преступлений', 'template': 'students_book/paragraph7.html'},
    8: {'title': 'Преступность несовершеннолетних и молодежи', 'template': 'students_book/paragraph8.html'},
    9: {'title': 'Международное сотрудничество в борьбе с преступностью', 'template': 'students_book/paragraph9.html'},
}


def paragraph_detail(request, paragraph_id):
    """Отображает страницу конкретной главы учебника."""
    paragraph = PARAGRAPHS.get(paragraph_id)
    
    if not paragraph:
        raise Http404(f"Глава {paragraph_id} не найдена")

    context = {
        'paragraph_id': paragraph_id,
        'paragraph_title': paragraph['title'],
    }
    
    return render(request, paragraph['template'], context)