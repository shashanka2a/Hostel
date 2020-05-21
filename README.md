We have made a Hostel Outing Management System using Django framework.We have developed two views,each for student and warden.Through this a student can fill the outing request form and submit.The warden gets a list of student requests and can approve/decline.Meanwhile student can check his/her request status in the dashborad.

## First-time setup

1.  Make sure Python 3.7x and Pipenv are already installed. [See here for help](https://djangoforbeginners.com/initial-setup/).
2.  Clone the repo and configure the virtual environment:

```
$ git clone https://github.com/shashanka2a/hostel
$ cd hostel
$ pipenv install
$ pipenv shell
```

3.  Set up the initial migration for our custom user models in `users` and build the database.

```
(djangox) $ python manage.py makemigrations users
(djangox) $ python manage.py migrate
```

4.  Create a superuser:

```
(djangox) $ python manage.py createsuperuser
```

5.  Confirm everything is working:

```
(djangox) $ python manage.py runserver
```

Load the site at [http://127.0.0.1:8000](http://127.0.0.1:8000).

![Home](static/images/home_2.2.png)

![Sign Up](static/images/signup_2.2.png)

