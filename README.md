# Servo 
Application showing the current distance from the entered location points


# New Features!

  - Find out information about your location
  - Find out what is your elevation


### Tech

* Python
* SQLAlchemy -Python SQL toolkit and Object Relational Mapper
* Flask - microframework for Python based on Werkzeug and Jinja 2
* Google Geolocation Api - returns a location and accuracy radius based on information about cell
* Bootstrap - great UI boilerplate for modern web apps
* Geopy - Client for several popular geocoding web services.
* HTML - Create your own Website
* GITHUB - https://github.com/LikeaBoooM/Servo



### Installation
```sh
install :

https://www.python.org/downloads/release/python-373/

Go to your command line and run this senences :

pip install Flask
pip install Flask-sqlalchemy
pip install Flask-bcrypt
pip install Flask-login
pip install pandas
pip install geopy
pip install flask-wtf
pip install googlemaps
pip install elevation

```
### Development

* Google Geolocation Api - returns a location and accuracy radius based on information about cell
* Geopy - Client for several popular geocoding web services.


## Unit testing

#### Distance test
```sh

Go to your commandline and run :

cd flaskb
cd flaskb
python geopy_test.py

```
This script checks if the Geopy API works


The result has to be OK 

#### Elevation test
```sh

Go to your commandline and run :

cd flaskb
cd flaskb
python elevation_test.py

```
This script checks if the elevation API works


The result has to be OK 


# How it works
```sh

Go to your commandline and run :

cd flaskb
python run.py


If server start :

SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
 * Serving Flask app "flaskb" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
C:\Users\Mati\AppData\Local\Programs\Python\Python37-32\lib\site-packages\flask_sqlalchemy\__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
 * Debugger is active!
 * Debugger PIN: 327-162-271
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


Go to your browser and enter :

http://localhost:5000/
```

* Firstly you have to register your account and log in

 
### Provide the correct data during registration
You can easly change data by entering Account Page

* Secondly, add your first location by entering in New Location 
### Provide the correct data during adding new location

After that come back to the home page.

Now you see your post and required information
(You can easly update posted information, by clicking on the title of the post and choosing update option)


In the post you will see:
* Geographical coordinates of the post
* Geographical coordinates of the current user
* Post's elevation
* Distance from the current user
* Information whether the location is within the range provided during registration 
####You can edit the scope of the current user and the post will update automatically

You can easly delete the post. Just click on the title and choose option delete



### Contact me, if you have any problems
* email : mborkowski010@gmail,com
* phone number : 508 681 793

I am available 24/7




   