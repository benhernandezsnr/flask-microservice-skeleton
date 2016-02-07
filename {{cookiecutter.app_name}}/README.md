# Flask Microservice Skeleton

The Flask Microservice Skeleton provides a starting point for a typical Flask based application server

- Docker based development environment
- Setup integration tests with coverage
- Master/slave database connections (planned)

# Getting Started

## 1. Clone the repository
    
    $ git clone xyz

## 2. Bring up the development environment
    
    $ docker-compose up

## 3. Check the server is running

    $ curl http://localhost:5000/health/ping
    {
      "status": "success"
    }

## 4. Initialize the database

    $ ./container_manage.sh db upgrade

## 5. Play with the api

    $ curl -H "Content-Type: application/json" -X POST -d '{"name":"Larry"}' http://localhost:5000/v1/skeleton
    {
      "result": {
        "id": 1, 
        "name": "Larry"
      }
    }

    $ curl http://localhost:5000/v1/skeleton
    {
      "result": [
        {
          "id": 1, 
          "name": "Larry"
        }
      ]
    }

# Tasks

## 1. Run Integration Tests

    tox -e test

## 2. Connect to database

    mysql -h 127.0.0.1 -P 3306 -u dev --password=test {{cookiecutter.db_name}}

## 3. Adding a python dependancy

First update app/setup.py with the new package

Tell docker-compose to rebuild its images

    docker-compose down
    docker-compose build

Once complete start again with

    docker-compose up

## 4. Adding a Database migration

flask-microservice uses [flask-migrate](https://flask-migrate.readthedocs.org/en/latest/) to update the database based on contents of the models/ directory.

The development pattern to follow is to

1. update models/ as needed
2. create a migration file

    $ ./container_manage.sh db migrate

This will create a migration in the migrations/versions directory

3. run the migration against the database

    $ ./container_manage.sh db upgrade

# Tips

# 1. Running a command in the webserver container

For example lets list the packages installed in the webserver container
    
    docker exec flaskmicroservice_web_1 pip list

Lets install a pip package in the server

    docker exec flaskmicroservice_web_1 pip install nosetests

Manually run tests

    docker exec flaskmicroservice_web_1 nosetests -s tests

# Overview

1. The code is arranged so that app is package [see](http://flask.pocoo.org/docs/0.10/patterns/packages/)