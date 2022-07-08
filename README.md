# Django REST Framework Starter Template

This is a template for DRF with Custom User Model for quickly starting a DRF Project

This template includes `BaseModel`, `DynamicFieldsModelSerializer`, Custom `User` Model and logging capabilities.

## Project Structure

```
drf-starter-template.
|   manage.py
|   README.md
|   requirements.txt
|
+---core
|   |   admin.py
|   |   apps.py
|   |   managers.py
|   |   models.py
|   |   serializers.py
|   |   tests.py
|   |   views.py
|   |   __init__.py
|   |
|   \---migrations
|           __init__.py
|
+---logs
|       project_name.log
|
+---project_name
|   |   .env.example
|   |   asgi.py
|   |   settings.py
|   |   urls.py
|   |   wsgi.py
|   |   __init__.py
|
\---users
    |   admin.py
    |   apps.py
    |   models.py
    |   serializers.py
    |   tests.py
    |   views.py
    |   __init__.py
    |
    \---migrations
            __init__.py

```


## Dependencies


Django
> Obviously ;)

[djangorestframework](https://django-rest-framework.org)
> DRF

[django-cors-headers](https://github.com/adamchainz/django-cors-headers)
> For CORS Headers

[django-environ](https://django-environ.readthedocs.io/en/latest/)
> To use environment variables from `.env` file

[django-extensions](https://django-extensions.readthedocs.io/)
> To access Advanced Django Shell

[django-filter](https://django-filter.readthedocs.io/)
> For multiple complex filters

[django-model-utils](https://django-model-utils.readthedocs.io/)
> For Base Model

[djoser](https://djoser.readthedocs.io/)
> For Token Authentication

[drf-yasg](https://drf-yasg.readthedocs.io/)
> Swagger Generator


## Setup

Setup `.env` in your project settings.

`.env.example` is provided for reference


### Start Django Project using `template` argument

`django-admin startproject <my_project> --template https://github.com/wh0th3h3llam1/drf-starter-template.git`

### Makemigrations

`python manage.py makemigrations`

> Note: Default Database is SQLite3. It can be configured in `.env`

### Migrate

`python manage.py migrate`
