# Awwwards

    Author: Ngige Brian

## Description

This project allows users to post their projects for other users to rate according to design, usability and content

### User Story

* A user can view posted projects and their details.
* A user can post a project to be rated/reviewed.
* A user can rate/ review other users' projects.
* Search for projects.
* View projects overall score.
* A user can view their profile page.

#### Setup and Installation

* Cloning the repository:
  * <https://github.com/JeremiahNgige/awwwards.git>

* Navigate into the folder and install requirements
  * cd awwards pip install -r requirements.txt

* Install and activate Virtual
  * python3 -m venv virtual - source virtual/bin/activate  

* Setup Database
* SetUp your database User,Password, Host then make migrate
  * python manage.py makemigrations

* Now Migrate
  * python manage.py migrate

* Run the application
  * python manage.py runserver

* Open the application on your browser 127.0.0.1:8000.

#### Technology used

* Python3.8
* Django 3.1.2
* Heroku

#### Known Bugs

The project did not work completely properly as expected

#### Contact Information

If you have any question or contributions, please email me at alexotieno900@gmail.com

#### License

* licensed under the [MIT license](LICENSE)
* Copyright &copy; 2020 | Jeremiah Brian
