# 📘 КРИМИНОЛОГИЯ — электронный учебник

**«КРИМИНОЛОГИЯ (общая часть)»** — веб-приложение электронного учебника для курсантов, слушателей и преподавателей Московского университета МВД России имени В.Я. Кикотя.

Приложение предоставляет структурированный доступ к материалам курса: главам и параграфам учебника, справочной информации, библиографии и дополнительным PDF- и видеоматериалам.

🌐 **Развёрнутая версия:** https://criminology-studentsbook.onrender.com/

## ✨ Основные возможности

* 📖 Навигация по **9 главам** учебника и их параграфам
* 📝 Отдельные страницы с аннотацией, введением и заключением
* 📚 Глоссарий основных понятий
* 📑 Библиографический список
* 📄 Просмотр встроенных PDF-документов
* 🎥 Работа с видеоматериалами
* 📱 Адаптивный интерфейс для компьютеров, планшетов и смартфонов
* ⬆️ Быстрая навигация по длинным страницам
* 🎨 Единый шаблон страниц и переиспользуемые элементы интерфейса

## 🛠 Технологии

* **Python 3**
* **Django 3.2.16**
* **HTML5 / CSS3**
* **Bootstrap 5**
* **Bootstrap Icons**
* **SQLite**
* **WhiteNoise**
* **Gunicorn**
* **Git / GitHub**
* **Render**

## 🏗️ Архитектура

Приложение построено на Django и разделено на несколько функциональных частей:

* `pages` — информационные страницы: аннотация, введение, заключение, глоссарий и библиография;
* `students_book` — структура и содержание глав учебника;
* `templates` — общие HTML-шаблоны и переиспользуемые компоненты;
* `static` — CSS, изображения и медиаматериалы.

Для информационных страниц используются Django `TemplateView`, что позволяет отделить представление статического контента от структуры проекта.

## 🚀 Запуск проекта

### Клонирование

```bash
git clone https://github.com/oayaivaivb/criminology_studentsbook.git
cd criminology_studentsbook
```

### Создание виртуального окружения

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Миграции

```bash
python manage.py migrate
```

### Запуск

```bash
python manage.py runserver
```

Приложение будет доступно по адресу:

```text
http://127.0.0.1:8000/
```

## 🌐 Деплой

Проект развёрнут на **Render** как отдельный Web Service.

Сборка выполняется с помощью `build.sh`:

```bash
pip install -r requirements.txt
python criminology_students_book/manage.py collectstatic --no-input
python criminology_students_book/manage.py migrate --no-input
```

Для запуска production-приложения используется **Gunicorn**:

```bash
gunicorn criminology_students_book.wsgi
```

Статические файлы обслуживаются через **WhiteNoise**.

## 🔐 Конфигурация

Чувствительные параметры приложения не хранятся непосредственно в коде.

Используются переменные окружения:

```env
DJANGO_SECRET_KEY=your_secret_key
DJANGO_DEBUG=False
PYTHON_VERSION=3.x
```

`SECRET_KEY` и режим `DEBUG` считываются из переменных окружения, а production-конфигурация разрешает работу приложения на доменах Render.

## 📁 Структура проекта

```text
criminology_studentsbook/
├── criminology_students_book/
│   ├── criminology_students_book/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── pages/
│   │   └── ...
│   ├── students_book/
│   │   └── ...
│   ├── templates/
│   │   ├── base.html
│   │   └── includes/
│   ├── static/
│   │   ├── css/
│   │   ├── img/
│   │   └── media/
│   └── manage.py
├── build.sh
├── requirements.txt
├── .gitignore
└── README.md
```

## 📚 Содержание

Учебник посвящён общей части криминологии и включает материалы по следующим направлениям:

* понятие, предмет, система и функции криминологии;
* преступность и её основные характеристики;
* причины и условия преступности;
* личность преступника;
* механизм индивидуального преступного поведения;
* виктимология;
* предупреждение преступлений;
* криминологическое прогнозирование и планирование;
* организация криминологических исследований.

## 🔗 Ссылки

* 🌐 **Веб-приложение:** https://criminology-studentsbook.onrender.com/
* 💻 **GitHub:** https://github.com/oayaivaivb/criminology_studentsbook
