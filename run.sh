#!/bin/sh

if [ $1 != "-n" ]; then
	python -m pipenv install
fi
python -m pipenv run python manage.py runserver
