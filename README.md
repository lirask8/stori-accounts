#### Technologies

  * [Django](https://www.djangoproject.com/)
  * [Django Rest Framework](http://www.django-rest-framework.org/)

You need to have installed `git`, `docker`, `ssh`.

#### Basic commands for running project
  * `git clone git@github.com:lirask8/stori-accounts.git` Clone the project.
  * `cd stori-accounts`
  * `docker-compose build` build the images for development.
  * `docker-compose run web python manage.py createsuperuser` create a superuser for admin interface
  * `docker-compose run web python manage.py loaddata users accounts` load fixtures
  * `docker-compose up` run the server

##### Now you can execute endpoint POST localhost:8000/transactions/process-file/ with account_id and file (transactions.csv on root dir) parameters
* You can use the Postman collection in docs directory, there are others endpoints for accounts creations
![postman](https://public-images-ols3.s3.us-east-2.amazonaws.com/postman.png)



### Run django admin and mailhog ui

* [http://localhost:8000/admin/](http://localhost:8000/admin/)
* [http://localhost:8026/#](http://localhost:8026/#)

##### You can access to the saved transactions in database using admin ui:

![admin](https://public-images-ols3.s3.us-east-2.amazonaws.com/admin.png)

##### You can see the sent e-mail using mailhog ui:

![mailhog](https://public-images-ols3.s3.us-east-2.amazonaws.com/mailhog.png)



#### Other functional commands
  * `docker-compose run --service-ports web` Debug console
  * `docker-compose run web python manage.py makemigrations` make the migrations
  * `docker-compose run web python manage.py migrate` apply the migrations