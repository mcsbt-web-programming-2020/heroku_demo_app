# Heroku demo app

## Running the app locally

### Creating the virtualenv

```
virtualenv venv
. venv/bin/activate
```

### Creating tables locally

First of all, we'll need to create the tables in the DB:

```
$ python
Python 3.7.5 (default, Oct 14 2019, 23:08:55)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> from server import db
/home/pepe/projects/mcsbt-advanced-python-2020/heroku_demo_app/venv/lib/python3.7/site-packages/flask_sqlalchemy/__init__.py:814: UserWarning: Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. Defaulting SQLALCHEMY_DATABASE_URI to "sqlite:///:memory:".
  'Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. '
/home/pepe/projects/mcsbt-advanced-python-2020/heroku_demo_app/venv/lib/python3.7/site-packages/flask_sqlalchemy/__init__.py:835: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

^^^^^^ At this point, hit ctrl-c to stop the previous process ^^^^^^^

>>> db.create_all()
>>> exit()
```


### Running the local server

Now we have all tables created in the DB, let's run the server:


```
$ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

## Running on Heroku

### Creating the heroku app

make sure you're `cd`ed into this folder and then:

```
$ heroku create
```

(if you haven't before, you'll need to `heroku login`)

### Creating DB in Heroku

You can create a database for your project in Heroku as follows:

```
heroku addons:add heroku-postgresql:hobby-dev
```

This will create a new database in heroku postgres and also will add
an environment variable `DATABASE_URL` with the database connection
string.

### Creating tables in Heroku

We can get a python console from our heroku application running:

```
$ heroku run python
Python 3.7.5 (default, Oct 14 2019, 23:08:55)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> from server import db
/home/pepe/projects/mcsbt-advanced-python-2020/heroku_demo_app/venv/lib/python3.7/site-packages/flask_sqlalchemy/__init__.py:814: UserWarning: Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. Defaulting SQLALCHEMY_DATABASE_URI to "sqlite:///:memory:".
  'Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. '
/home/pepe/projects/mcsbt-advanced-python-2020/heroku_demo_app/venv/lib/python3.7/site-packages/flask_sqlalchemy/__init__.py:835: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

^^^^^^ At this point, hit ctrl-c to stop the previous process ^^^^^^^

>>> db.create_all()
>>> exit()
```

As you see, we run **the same** commands as locally for creating the
db tables.

### Pushing to heroku

Once our app is connected to heroku (we can check that with `git
remote -v`), we can just `git push heroku master` to deploy our
application.
