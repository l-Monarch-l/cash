Это веб-приложение для учета движения денежных средств (ДДС)

Использовалось:
Backend: Django (Python)
Frontend: HTML, Bootstrap 5
База данных: PostgreSQL (в Docker)
Инфраструктура: Docker, Docker Composeб
Также работа выполнилась при помощи poetry

Инстркуция по запуску:
1. Клонирование репозитория
   git clone https://github.com/l-Monarch-l/cash
   переходим в cd cash-flow-app
3. Собираем docker
   docker-compose up --build
   переходим по ссылку и проверяем работу http://localhost:8000/dds/
