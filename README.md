# python_server_eng_exercise

## setup
python3 -m pip install -r requirement.txt

## database
psql
CREATE DATABASE data

## start the server
uvicorn run:app --host 127.0.0.1 --port 5081

## Run unit tests
 pytest -c app/tests/pytest.ini

## Check the OpenAPI docs
In development mode, OpenAPI documentation is available at

http://127.0.0.1:5081/v1/api-doc


