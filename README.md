# SmartCook API

# Environment setup
## Virtual Environment
First, you need to create a virtual environment for the project,
```python
python3 -m venv SmartCook_API_venv
```
activate it,
```python
source SmartCook_API_venv/bin/activate
```
and finally install the packages listed in `requirements.txt`
```python
pip3 install -r requirements.txt
```
then you must configure your preferred IDE to use that venv as interpreter.

## Database creation
```python
psql -d postgres
create database smartcook;
create database smartcook_test;
```

## `.env` file
The following content must be added in your local `.env` file in order to run
the API:
```python
# settings.py
SECRET_KEY = ...
DEBUG = True

# database
DB_NAME = smartcook
DB_USER = your_user
DB_PASSWORD = your_password
DB_HOST = localhost
DB_PORT = 5432
```
# Run the API
```python
python3 manage.py runserver
```

# Deployment
For the moment we don't have resources for a staging domain, thus we'll be
using
## Staging
