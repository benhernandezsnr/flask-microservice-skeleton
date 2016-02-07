#!/bin/bash

docker exec {{cookiecutter.app_name}}_web_1 python manage.py $@