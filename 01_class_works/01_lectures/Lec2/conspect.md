## Установка Django

* ```pip install django```

# Первым делом необходимо создать проект

**Проект** - голова всей разработки.Для того, чтобы создать проект необходимо выполнить команду:
* ```django-admin startproject hello .```
* ```hello``` - имя проекта
* Внутри директории ```hello``` лежит средце проекта ```settings.py``` , а также информация для конфигурации локального сервера (```asgi.py```, ```wsgi.py```)

## Запуск проекта с дефолтным функицоналом
* ```python manage.py runserver```

* ```manage.py``` - "руль" проекта. Через него происходит все внешние коммуникации (запуск сервера, создание/апдейт БД, запуск тестов, реконфиг сервера и т.д.)

## Для решения проблемы контроля зависимостей проекта 
Создадим виртуальное окружение и будем работать в нем. Для установки утилиты создания виртуальных окружений:
* ```pip install pipenv```

Теперь необходимо создать первое окружение:
```pipenv shell```

Чтобы закрыть окружение: ```exit```

Чтобы запустить окружения со сторонними ```pipfile```'ми - ```pipenv install```

Установим Django внутрь нашего окружения:
* ```pipenv install django``` (в старых версиях нужно было ```pip install django``` < 3.7)

# Основная задача pipenv - контролировать версии сторонних зависимостей