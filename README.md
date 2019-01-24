# iReporter-Database
[![Build Status](https://travis-ci.org/Emmanuelaaron/iReporter-Database.svg?branch=develop)](https://travis-ci.org/Emmanuelaaron/iReporter-Database)
[![Coverage Status](https://coveralls.io/repos/github/Emmanuelaaron/iReporter-Database/badge.svg?branch=develop)](https://coveralls.io/github/Emmanuelaaron/iReporter-Database?branch=develop)

Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

## Getting started
You can clone this [repo](https://github.com/Emmanuelaaron/iReporter-Database.git) on your local machine or checkout the user-interface on [gh-pages](https://emmanuelaaron.github.io/iReporter/UI/temps/start_page) and the app is hoted on [heroku](https://ireporter-d-b.herokuapp.com/api/v2)

### Prerequisites
Install [python](https://www.python.org/downloads/release/python-371/) on your local machine

### Installing
Clone the this repo on your local machine
```
$ git clone https://github.com/Emmanuelaaron/iReporter-Database.git
```
cd into the cloned directory, install the virtual environment and activate, checkout to the most stable branch and install all the dependences.
```
$ cd iReporter-database
$ pip install virtualenv
$ virtualenv venv
$ source venv/Scripts/activate
$ git checkout develop
$ pip install -r requirements.txt
$ python run.py
```
* copy the Url it into postman and put to run any endpoint of your preference in the table below with the url prefix ('/api/v2') for each endpoint.

HTTP Method | Endpoint | Functionality | Parameters 
------------|----------|---------------|------------
POST | /auth/signup | User is able to signup | None
POST | /auth/login | User is able to login | None
POST | /incidence | Creates incidences| None
GET | /interventions| Gets all interventions| None
GET | /red-flags | Gets all red flags | None
GET | /interventions/<int:incident_id> | Gets a specific intervention | incident_id 
GET | /red-flags/<int:incident_id> | Gets a specific red flag | incident_id
DELETE | /interventions/<int:incident_id> | Deletes a specific intervention | incident_id
DELETE | /red-flags/<int:incident_id> | deletes a specific red flag | Flag_id

## Running Tests
Install pytest, activate the virtual environment and then run the tests
```
$ pip install pytest
$ pytest
```
You can checkout the code coverage by using the code below
```
$ pytest --cov=.
```
Make sure your virtual environment is activated

## Deployment
The application is hosted on [heroku](https://ireporter-d-b.herokuapp.com/api/v2)

## Tools Used
* [python](https://www.python.org/downloads/release/python-371/)
* [Flask](http://flask.pocoo.org/) Micro web framework for python
* [pip](https://pip.pypa.io/en/stable/) package installer for python
* [Virtualenv](https://virtualenv.pypa.io/en/stable/) Tool used to created isolated programs for python
* [Postgresql](https://www.postgresql.org/docs/11/index.html)

## Built with
So far this application has been built with
* [Python](https://www.python.org/downloads/release/python-371/)
* [Flask](http://flask.pocoo.org/)
* [Postgresql](https://www.postgresql.org/docs/11/index.html)


## Contributions
To contribute to this project please create a branch off the develop after which you will create a pull request before it is merged back.

## Aurthor
By Emmanuel Isabirye
