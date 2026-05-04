#!/usr/bin/env bash
# Выход при ошибке
set -o errexit

# Установка зависимостей
pip install -r requirements.txt

# Сбор статики
python criminology_students_book/manage.py collectstatic --no-input

# ПРИМЕНИТЬ МИГРАЦИИ (ОБЯЗАТЕЛЬНО!)
python criminology_students_book/manage.py migrate --no-input