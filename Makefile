up:
	docker compose up -d

upb:
	docker compose up --build

down:
	docker compose down

down-v:
	docker compose down -v

run:
	python manage.py runserver 0.0.0.0:8000

collectstatic:
	python manage.py collectstatic --noinput

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

superuser:
	python manage.py createsuperuser_credentials

pre-commit:
	pre-commit install

