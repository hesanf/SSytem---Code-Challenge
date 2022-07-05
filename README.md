# ssystem_npm
a rest api using django that loads 5 latest news from this link: “https://feeds.npr.org/1004/feed.json”

Hello Dear 

some things you should do after cloning listed below :
1. start a new virutal env. using : pipenv shell
2. then you must install dependecies using : pipenv install
3. make migrations using : python manage.py makemigrations
4. apply migrations to db : python manage.py migrate 
5. you must create a new superuser for browsing admin panel : django-admin createsuperuser (choose "demo" for both field for default)
6. then run the project on your localhost : python manage.py runserver (default is http://127.0.0.1:8000)

then navigate to localhost:8000 for API
and localhost:8000/admin/ for admin area