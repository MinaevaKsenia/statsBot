# Telegram бот сбора статистики по данным из базы данных

В проекте реализована серверная часть бота по сбору статистики на основе данных из базы данных, собранной на форуме dccomics.ru. Для разработки использовался фреймворк Flask.

#### Порядок запуска для локального тестирования:
- Развернуть виртуальное окружение
- Активировать виртуальное окружение /venv/Scripts/activate
- Установить зависимости проекта из файла requirements.txt
- Установить переменную окружения FLASK_APP на main.py
- Установить переменную окружения PYTHONPATH на папку src
- Находясь в папке проекта и имея активированное виртуальное приложение запустить встроенный Flask сервер командой flask run. По умолчанию сервер будет доступен по адресу: 127.0.0.1:5000.

#### Доступные маршруты:
#### 1. Получение общих данных
/acquisition/type, где type в промежутке от 1 до 4 в зависимости от типа получаемых данных.
#### 2. Получение данных о конкретном пользователе
/acquisition/username/type, где username - имя пользователя, type в промежутке от 1 до 2, в зависимости от типа получаемых данных.
#### 3. Получение списка пользователей
/acquisition
