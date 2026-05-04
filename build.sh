#!/usr/bin/env bash
# Выход при ошибке
set -o errexit

# Установка зависимостей
pip install -r requirements.txt

# Сбор статики (CSS, JS, картинки)
python criminology_students_book/manage.py collectstatic --no-input

# Если вдруг когда-то появится БД, раскомментируй строку ниже:
# python criminology_students_book/manage.py migrate