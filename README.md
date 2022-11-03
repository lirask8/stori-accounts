#### Technologies

  * [Django](https://www.djangoproject.com/)
  * [Django Rest Framework](http://www.django-rest-framework.org/)

You need to have installed `git`, `docker`, `ssh`.

#### Basic commands for running project
  * `git clone git@github.com:lirask8/stori-accounts.git` Clone the project.
  * `cd stori-accounts`
  * `docker-compose build` build the images for development.
  * `docker-compose run web python manage.py createsuperuser` create a superuser
  * `docker-compose run web python manage.py loaddata users accounts` load fixtures
  * `docker-compose up` run the server
  * `docker-compose run web python manage.py test` run the tests


#### Other functional commands
  * `docker-compose run --service-ports web` Debug console
  * `docker-compose run web python manage.py makemigrations` make the migrations
  * `docker-compose run web python manage.py migrate` apply the migrations


### Run django admin and mailhog ui

* [http://localhost:8000/admin/](http://localhost:8000/admin/)
* [http://localhost:8025/#](http://localhost:8026/#)
