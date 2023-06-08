up:
	docker compose up -d

run:
	python manage.py runserver 0.0.0.0:8000

upb:
	docker compose up --build

pre-commit:
	pre-commit install

