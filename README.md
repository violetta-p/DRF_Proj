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

Настройка сервера:
    Установите необходимое ПО на сервере:
        sudo apt-get update
        sudo apt-get install postgresql postgresql-contrib python3-pip
    
Создайте базу данных и пользователя PostgreSQL для вашего проекта:
        sudo -u postgres psql
        CREATE DATABASE yourdbname;
        CREATE USER yourdbuser WITH PASSWORD 'yourpassword';
        ALTER ROLE yourdbuser SET client_encoding TO 'utf8';
        ALTER ROLE yourdbuser SET default_transaction_isolation TO 'read committed';
        ALTER ROLE yourdbuser SET timezone TO 'UTC';
        GRANT ALL PRIVILEGES ON DATABASE yourdbname TO yourdbuser;

Установите необходимые Python-пакеты на сервер с помощью pip:
        pip3 install virtualenv

Скопируйте свой Django-проект на сервер (например, через git clone или через SCP).

Настройка Gunicorn и systemd:
        1. Создайте виртуальное окружение для вашего проекта:
                virtualenv venv
                source venv/bin/activate

        2. Установите зависимости проекта:
                pip install -r requirements.txt

        3. Создайте unit-файл для systemd (например, yourproject.service) для управления Gunicorn как сервисом. Пример unit-файла:

Пример Unix-файла
[Unit]
Description="project_name" daemon
After=network.target

[Service]
User=your_username # Имя пользователя владельца проекта в Linux
Group=your_groupname # Группа, к которой относится пользователь
WorkingDirectory=/path/to/your/project # Путь к рабочей директории проекта
ExecStart=/path/to/venv/bin/gunicorn --config /path/to/gunicorn_config.py your_project.wsgi:application
# Команда для запуска проекта

[Install]
WantedBy=multi-user.target # Ожидание запуска системы в нормальном состоянии доступа для пользователей


Запустите и активируйте сервис:
sudo systemctl start project_name
sudo systemctl enable project_name


###Автор проекта:
@Viit_115


