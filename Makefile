DOCKER = docker-compose run app

help:
	@echo "------------HELP------------"
	@echo "To test project run make test"
	@echo "----------------------------"

test:
	${DOCKER} python manage.py test
