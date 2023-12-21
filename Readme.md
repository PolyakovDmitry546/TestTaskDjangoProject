## Реализован Django + Stripe API бэкенд со следующим функционалом:
- Django Модель Item с полями (name, description, price)
- API с двумя методами:
    - GET /buy/{id};
    - GET /item/{id};
- Добавлен Dockerfile для сборки проекта
- Используются environment variables:
    - STRIPE_SECRET_KEY
    - STRIPE_PUBLIC_KEY
    - SECRET_KEY
- Добавлен просмотр модели Item в Django Admin панели

