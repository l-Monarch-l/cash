Это веб-приложение для учета движения денежных средств (ДДС)

технологии:

Backend: Django (Python)

Frontend: HTML, Bootstrap 5

База данных: PostgreSQL (в Docker)

Инфраструктура: Docker, Docker Compose, poetry


Инстркуция по запуску:
1. Клонирование репозитория
   
   ```git clone https://github.com/l-Monarch-l/cash```
   
   ```cd cash-flow-app```
   
3. Собираем docker
   
   ```docker-compose up --build```
   
   переходим по ссылке и проверяем работу ```http://localhost:8000/dds/```

Автор: l-Monarch-l

Важные команды

```docker-compose exec web python manage.py createsuperuser``` - Создать админа

```poetry add package-name```	- Добавить зависимость

установить все зависимости из pyproject.toml
```poetry install```

скришноты:
![image](https://github.com/user-attachments/assets/59ff9f75-4e53-4553-b2cf-d6358c49f6af)

![image](https://github.com/user-attachments/assets/e30a57b6-a142-4082-8ba4-cc20522b8361)

![{065394BE-2BA9-45D1-9625-D255ADD5524B}](https://github.com/user-attachments/assets/b9b66aac-0baf-4dbf-a916-2e7e281fe40d)

![image](https://github.com/user-attachments/assets/4d470896-f271-4f9b-9236-f5b7ac469ec6)

![image](https://github.com/user-attachments/assets/a706b4f5-23ee-4662-ad0d-57cafda903f8)

![image](https://github.com/user-attachments/assets/208bfcb2-baa9-4a09-9fe2-5a403ce282fe)



