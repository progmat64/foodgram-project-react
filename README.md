# Учебный проект: Foodgram - продуктовый помощник

[![Python](https://img.shields.io/badge/-Python-464641?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-464646?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![Postman](https://img.shields.io/badge/Postman-464646?style=flat-square&logo=postman)](https://www.postman.com/)

## Описание
"Foodgram" – это уникальная социальная платформа, где кулинарные мастера могут поделиться своими самыми изысканными рецептами. Авторизованные пользователи имеют возможность публиковать свои собственные рецепты, подписываться на публикации других талантливых поваров и добавлять наиболее понравившиеся рецепты в список «Избранное». Кроме того, пользователи могут легко скачать сводный список продуктов, необходимых для приготовления выбранных блюд. Даже неавторизованные пользователи могут наслаждаться просмотром рецептов и страниц авторов.

Присоединяйтесь к "Foodgram" и откройте для себя бесконечное море кулинарных вдохновений!

## Чтобы запустить проект локально, выполните следующие действия

```bash
git clone git@github.com:Alexandr6400/foodgram-project-react.git

python3 -m venv venv
source venv/bin/activate

cd backend
pip install -r requirements.txt

cd foodgram
python manage.py migrate
python manage.py createsuperuser

```bash
# Перейти в дерикторию foodgram-project-react 
cd infra
docker compose up --build

cd backend/foodgram
python manage.py runserver
```