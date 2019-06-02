install:
	pipenv install

migrations:
	python manage.py makemigrations
	python manage.py migrate

start:
	python manage.py runserver 0.0.0.0:8000

docker:
	docker-compose up -d --build

