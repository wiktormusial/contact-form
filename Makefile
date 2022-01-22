DOCKER = docker-compose run app

help:
	@echo "-----------------HELP-----------------"
	@echo "To test project run make test"
	@echo "To migrate run make migrate"
	@echo "To make migrations on contact run make migrations_contact"
	@echo "---------------------------------------"

test:
	${DOCKER} python manage.py test

migrate:
	${DOCKER} python manage.py migrate

migrations_contact:
	${DOCKER} python manage.py makemigrations contact
