# Price Sync System

This is the backend of the price_sync_system project, which is a RESTful API developed using Python 3.9.6 as the programming language, Flask 2.3.2 as the web framework, SQLAlchemy 2.0.17 as the ORM, and PostgreSQL as the database engine.


## Project Overview
This is a RESTful API that consists of 4 main API endpoints:

### Endpoints
- /inventory: Used for the manipulation of inventory records in the database.
- /auth: Handles user authentication and permission validation.
- /roles: Provides access to role information and the users associated with each role.
- /users: Allows modification of user information.

The detailed documentation of the endpoints can be found here.

## Requirements
- Python 3.9.6 (Using a different version may lead to certain errors)
- Access to a database with the Postgresql engine
- Docker (If you plan to launch for production)


## Installation for development

First, we prepare the environment by going into the dev branch and installing the dependencies listed in the requirements.txt file.
```
git checkout dev
pip install -r requirements.txt
```
Pytest is the testing framework used in the project. By default, it is not included in the requirements.txt file, so you need to install it manually
```
pip install pytest
```
Update the user, password, and host in the DATABASE_URI found in the dev.py and test.py files.
```
[scripts/dev.py]

os.environ['DATABASE_URI'] = 'postgresql://[user]:[password]@[host]/price_sync_system_prod_dev'
```
```
[scripts/test.py]

os.environ['DATABASE_URI'] = 'postgresql://[user]:[password]@[host]/price_sync_system_prod_test'
```


## Development 
To start the local development server you must run the development script in the scripts directory
```
python scripts/dev.py
```
To launch the tests you must use the test.py script in the scripts folder
```
python scripts/test.py
```
The test.sh script accepts all pytest parameters

The dev.py and test.py file exist to make it easier to initialize the environment variables used by the app.

## Installation for production
First, we choose the release we want to run
```
git checkout release.
```
Seccond, We prepare the environment installing the dependencies listed in the requirements.txt file.
```
pip install -r requirements.txt
```
Third, build the dockerfile from the directory giving it a name, in this case price_sync_apirest_prod
```
docker build -t price_sync_apirest_prod .
```
## Start app in production 
We start the container by passing it two environment variables necessary for the project to work.
The first variable represents the URI of the production database, and the second variable is the secret key used by the app.

Attention:
- Replaces the values in braces according to your database configuration.
- Replace the SECRET_KEY value with another, this value must be fixed throughout the use of the app, both passwords and other data use this SECRET_KEY
- Database "price_sync_apirest_prod" must be created before starting the container
```
sudo docker run -e DATABASE_URI='postgresql://[user]:[password]@[host]/price_sync_apirest_prod' -e SECRET_KEY="abcdfg2020" --network host price_sync_apirest_prod

```

  
  
  .
  




