# python_server_eng_exercise

## setup

## Bring up the stack
docker-compose up --build -d

## database
postgres : 
CREATE DATABASE data

## start the server
uvicorn run:app --host 127.0.0.1 --port 5081

## start server using docker
docker-compose up

## Run unit tests
 pytest -c app/tests/pytest.ini

## Check the OpenAPI docs
In development mode, OpenAPI documentation is available at

http://127.0.0.1:5081/v1/api-doc


