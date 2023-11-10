Данный проект представляет собой бэкенд-часть SPA веб-приложения.
Проект онлайн-обучения позволяет пользователю создавать собственные курсы и уроки, 
а также просматривать уроки других пользоввателей.

## Используемые технологии

  * Язык: python (версия интерпретатора python - 3.11.)
  * Фреймфорк: django (Django REST framework)
  * БД (СУБД) проекта: PostgreSQL
  * python
  * drf-yasg
  * redis
  * celery, django-celery-beat
  * cors
  * jwt (simple jwt)


## Документация API
Документация для API реализована с помощью drf-yasg и находится на следующих эндпоинтах:
* http://127.0.0.1:8000/redoc/ - ссылка на редок
* http://127.0.0.1:8000/docs/ - ссылка на сваггер

## CORS
Для безопасности API реализован CORS с помощью django-cors-headers. 

В модуле ``settings.py`` необходимо внести изменения в следующие настройки, 
если у вас есть сторонние домены, обращающиеся к вашему API:

```
CORS_ALLOWED_ORIGINS = [
    "https://read-only.example.com",
    "https://read-and-write.example.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://read-and-write.example.com",
]
```

## Запуск проекта
* Склонировать репозиторий в IDE: 
   В терминале ввести команду: git clone https://github.com/violetta-p/DRF_Proj

* Установить виртуальное окружение и зависимости из файла requirements.txt:

  Ввести следующие команды в терминале:
  1. Создать виртуальное окружение: python3 -m venv venv
  2. Активировать виртуальное окружение: venv\Scripts\activate.bat (Windows), 
                                         source venv/bin/activate (Linux)
  3. Установить зависимости: pip install -r requirements.txt 
  4. Создать файл .env по шаблону из файла .env.sample

* Создать БД с названием, указанным в шаблоне (в пункте 4)

* Создать таблицы в БД. Создать миграции:
      python manage.py makemigrations
      python manage.py migrate

* Запустить redis и celery для работы периодических задач:

Linux:
1. Запуск брокера: 
 sudo systemctl start redis
2. Запуск обработчика задач:
 celery -A config worker -l info
 celery -A config beat -l info -S django

Windows:

1. Запуск брокера: 
 Для установки и запуска redis на Windows воспользуйтесь WSL 
 или инструкцией: https://github.com/MicrosoftArchive/redis

2. Запуск обработчика задач:
 celery -A config worker -l info -P eventlet
 celery -A config beat -l info -P eventlet


* Запустить сервер: python manage.py runserver

* Работа с docker:
  1. Создать образы: docker-compose build
  2. Запустить контейнеры: docker-compose up


###Автор проекта:
@Viit_115


