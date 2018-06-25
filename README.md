#### PyIntern [![Build Status](https://travis-ci.org/lays147/PyIntern.svg?branch=master)](https://travis-ci.org/lays147/PyIntern)

Application developed to help Institutions to
offer intern opportunities to students of technology.

Project to validate the knowledge acquired at a
class on Federal Fluminense Universtiy.


#### Requirements
###### For better use, install it into a virtualenv.
- Python3
- Django
- django-taggit

```bash
  python setup.py install
```

#### How to Run
```bash
cd PyIntern
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
python manage.py test
python manage.py runserver
```
Open your browser and type:
```
127.0.0.1:8000/admin
```
On the Django Admin you will see the models, where you can insert, change
and delete a item into the models.

#### Development
To create a new submodule type:
```bash
python manage.py startapp app_name
cd app_name
mkdir tests
mv tests.py tests/test_my_app_thing.py
touch tests/__init__.py
```
