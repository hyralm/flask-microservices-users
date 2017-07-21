Flask App
===========

REQUIREMENTS
------------

The minimum requirement by this application template that your Web server supports:

1. Python 3.6
2. Postgres 9.6

SET UP DEVELOPMENT ENVIRONMENT
------------------------------
All commands should be executed from project folder

1. Install [python 3.6](https://www.python.org/downloads/)
2. Install [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
3. Install [postgres](https://www.postgresql.org/download/)
4. Create virtual environment 
~~~
virtualenv -p /path/to/python3.6 env
~~~
5. Activate virtual environment
~~~
source env/bin/activate
~~~
6. Install requirements
~~~
pip install -r requirements.txt
~~~
7. Set environment variables
(you may need to change the username and password depending on your local Postgres config.)
~~~
export APP_SETTINGS=app.config.DevelopmentConfig
export DATABASE_URL=postgres://postgres:postgres@localhost:5432/users_dev
export DATABASE_TEST_URL=postgres://postgres:postgres@localhost:5432/users_test
export SECRET_KEY=my_precious
~~~
8. Create databases
~~~
python manage.py recreate_db
~~~
9. Run migrations
~~~
python manage.py db migrate
python manage.py db upgrade
~~~
9. Run server and browse to [localhosh:5000](http://localhosh:5000)
~~~
python manage.py runserver
~~~

DEVELOPMENT WORKFLOW
------------------------------
- Activate virtual environment
~~~
source env/bin/activate
~~~
- Set environment variables
(you may need to change the username and password depending on your local Postgres config.)
~~~
export APP_SETTINGS=app.config.DevelopmentConfig
export DATABASE_URL=postgres://postgres:postgres@localhost:5432/users_dev
export DATABASE_TEST_URL=postgres://postgres:postgres@localhost:5432/users_test
export SECRET_KEY=my_precious
~~~
- Development new features
~~~
...
~~~
- Deactivate virtual environment
~~~
deactivate
~~~

DEVELOPMENT COMMANDS
--------------------
- recreate databases
~~~
python manage.py recreate_db
~~~
- seed database
~~~
python manage.py seed_db
~~~
- run unit tests
~~~
python manage.py test
~~~
- init migrations
~~~
python manage.py db init
~~~
- create migrations
~~~
python manage.py db migrate
python manage.py db upgrade
~~~
- run server
~~~
python manage.py runserver
~~~
- activate virtual environment
~~~
source env/bin/activate
~~~
- deactivate virtual environment
~~~
deactivate
~~~