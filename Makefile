up:
	docker compose up -d

upb:
	docker compose up --build

down:
	docker compose down

down-v:
	docker compose down -v

sh:
	docker compose exec -it web sh

djsh:
	docker compose exec -it web python manage.py shell
run:
	docker compose exec -it web python manage.py runserver 0.0.0.0:8000

collectstatic:
	docker compose exec -it web python manage.py collectstatic --noinput

migrations:
	docker compose exec -it web python manage.py makemigrations

migrate:
	docker compose exec -it web python manage.py migrate

superuser:
	docker compose exec -it web python manage.py createsuperuser_credentials

pre-commit:
	pre-commit install

poetry:
	docker compose exec -it web poetry $(cmd)

