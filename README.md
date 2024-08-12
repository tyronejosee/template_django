# Template: Django

<!-- TODO: Create better sintaxis -->

## Commands

```python
django-admin startproject config .
django-admin startapp utils

(env) pip install -r requirements/local.txt

(env) docker compose -f docker-compose.dev.yml up
(env) docker compose -f docker-compose.dev.yml up --build
(env) docker compose -f docker-compose.dev.yml stop
(env) docker compose -f docker-compose.dev.yml logs -f
(env) docker compose -f docker-compose.dev.yml start
(env) docker compose -f docker-compose.dev.yml restart <service>

(env) docker compose -f docker-compose.dev.yml exec web bash
(env) docker compose -f docker-compose.dev.yml exec web python manage.py makemigrations*
(env) docker compose -f docker-compose.dev.yml exec web python manage.py migrate
(env) docker compose -f docker-compose.dev.yml exec web python manage.py migrate <app_label> <migration_name>
(env) docker compose -f docker-compose.dev.yml exec web python manage.py showmigrations

(env) docker compose -f docker-compose.dev.yml exec web python manage.py createsuperuser
```
