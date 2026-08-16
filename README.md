[![CI/CD](https://github.com/ArtemShastunov/foodgram/actions/workflows/main.yml/badge.svg)](https://github.com/ArtemShastunov/foodgram/actions/workflows/main.yml)

Продуктовый помощник — сайт, на котором пользователи публикуют рецепты, добавляют чужие рецепты в избранное, подписываются на авторов и формируют список покупок.

## Возможности

- Регистрация и аутентификация пользователей
- Просмотр рецептов с фильтрацией по тегам
- Добавление рецептов в избранное
- Подписка на авторов
- Формирование списка покупок
- Скачивание списка покупок файлом
- Админ-зона для управления контентом

## Стек технологий

- Python 3.12
- Django 5.1
- Django REST Framework
- PostgreSQL 13
- Docker + Docker Compose
- Nginx
- GitHub Actions (CI/CD)
- Gunicorn

## Развертывание

### Локально

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ArtemShastunov/foodgram.git
cd foodgram
Создайте виртуальное окружение:

bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/macOS
# или venv\Scripts\activate  # Windows
Установите зависимости:

bash
pip install -r requirements.txt
Примените миграции:

bash
python manage.py migrate
Загрузите ингредиенты:

bash
python manage.py load_ingredients
Запустите сервер:

bash
python manage.py runserver
В Docker
Создайте файл .env в папке infra:

text
POSTGRES_USER=foodgram_user
POSTGRES_PASSWORD=foodgram_password
POSTGRES_DB=foodgram
DB_HOST=db
DB_PORT=5432
SECRET_KEY=your_secret_key
DEBUG=false
ALLOWED_HOSTS=*
DOCKER_USERNAME=artemdecide
Запустите контейнеры:

bash
cd infra
docker compose -f docker-compose.production.yml up -d
Создайте суперпользователя:

bash
docker exec infra-backend-1 python manage.py createsuperuser
Проект будет доступен по адресу http://localhost.

Примеры запросов к API
Регистрация
text
POST /api/auth/users/
{
    "email": "user@example.com",
    "username": "user",
    "first_name": "Иван",
    "last_name": "Иванов",
    "password": "password123"
}
Получение токена
text
POST /api/auth/token/login/
{
    "email": "user@example.com",
    "password": "password123"
}
Список рецептов
text
GET /api/recipes/
Фильтрация по тегам
text
GET /api/recipes/?tags=breakfast&tags=lunch
Документация
Спецификация API: /api/docs/

Админ-зона: /admin/

Автор
Артём Шастунов