# Image_resize_API
it an API it has some fields including Image field, therefore ,it can create and retrieve data. uploaded image will be automatically resize to 140*140.

In order to use this file, you need to install or have rest_framework, django_resized,.
Initally I assume you already have django and python 3.
python3 -m pip install rest-framework, python3 -m pip install django_resized. (these are the comments that I used to install and it work for me) some don't need python3 -m.
In order to use this, it host on port 8000.
To check or use the api, you need to run the server. The comment is (python3 manage.py runserver)
Before running the server, you need to make migration, comment is "python3 manage.py makemigrations", and after that "python3 manage.py migrate".
To get the list of data by using api "Localhost:8000/api/fish" you can check the list.
And the url to post or create the data "Locahost:8000/api/fish/new" you can use the table to upload data.
