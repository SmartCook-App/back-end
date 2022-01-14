# SmartCook API

# Environment setup
We use Docker for the development of the SmartCook API.
## Docker setup
1. Install `Docker Desktop` from [here](https://docs.docker.com/desktop/mac/install/). This
will keep running the docker daemon and help you to see running containers and apps, 
while providing more customization of Docker itself.
2. Check versions for `docker` and `docker-compose` on the Terminal:

```shell
$ docker --version
> Docker version 20.10.11, build dea9396
```
```shell
$ docker-compose --version
> docker-compose version 1.29.2, build unknown
```

if your getting something like this, you're ready to go to next step!


## Virtual Environment
We don't have Dev Containers yet, so first, you need to create a virtual environment
for the project,
```shell
python3 -m venv SmartCook_API_venv
```
activate it,
```shell
source SmartCook_API_venv/bin/activate
```
and finally install the packages listed in `requirements.txt`
```shell
pip3 install -r requirements.txt
```
then you must configure your preferred IDE to use that venv as interpreter.

## `.env` file
The following content must be added in your project `.env.development` file in order to run
the API locally:
```dotenv
# settings.py
SECRET_KEY = ...
DEBUG = True
DJANGO_ALLOWED_HOSTS = *

# database
DB_NAME = smartcook
DB_USER = your_username
DB_PASSWORD = your_password
DB_HOST = db
DB_PORT = 5432
```
don't forget to change the `DB_USER` and `DB_PASSWORD` depending on your Postgresql
local configuration.

# Run the API
```shell
docker-compose --env-file .env.development -f docker-compose.development.yml up --build
```
Only the first time it takes about 1-2 minutes to build be containers as the needed
images are downloaded, then the API will be available at <http://localhost:8000>.
