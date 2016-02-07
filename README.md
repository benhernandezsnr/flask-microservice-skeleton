# Flask Microservice Skeleton

The Flask Microservice Skeleton provides a solid starting point for a typical Flask based application server

- Docker based development environment
- Setup integration tests with coverage
- Master/slave database connections (planned)

# Getting Started

## 1. Run cookiecutter
    
    $ pip install cookiecutter
    $ cookiecutter https://github.com/benhernandezsnr/flask-microservice-skeleton.git

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