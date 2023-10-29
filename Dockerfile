# Укажите базовый образ с Python
FROM python:3.7

# Установите переменную окружения для неинтерактивного режима
ENV PYTHONUNBUFFERED 1

# Создайте и установите рабочую директорию в контейнере
WORKDIR /app

# Скопируйте файл зависимостей и установите их
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Скопируйте все файлы из текущей директории в рабочую директорию
COPY . /app/

# Запустите Django приложение
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
