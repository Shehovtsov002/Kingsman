# Используем официальный Python образ в качестве базового
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app
COPY . /app/

# Копируем файл с зависимостями и устанавливаем их
RUN pip install -r requirements.txt