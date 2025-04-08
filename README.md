Это веб-приложение для учета движения денежных средств (ДДС)

Использовалось:

Backend: Django (Python)

Frontend: HTML, Bootstrap 5

База данных: PostgreSQL (в Docker)

Инфраструктура: Docker, Docker Compose, poetry


Инстркуция по запуску:
1. Клонирование репозитория
   
   git clone https://github.com/l-Monarch-l/cash
   
   переходим в приложение

   cd cash-flow-app
   
2. Собираем docker
   
   docker-compose up --build
   
   переходим по ссылке и проверяем работу http://localhost:8000/dds/


Важные команды

```docker-compose exec web python manage.py createsuperuser``` - Создать админа

```poetry add package-name```	- Добавить зависимость
