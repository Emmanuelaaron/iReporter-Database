import unittest
from api import app
from flask import json
from database.db import Database_connection
import jwt


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.tester = app.test_client(self)
        self.db = Database_connection()
        self.db.create_tables()
        self.user = {
            "username": "isabirye",
	        "email": "ema@yahoo.com",
	        "firstname": "emma",
	        "lastname": "isabirye",
	        "othernames": "aaron",
	        "password": "gftdsjgg",
	        "phone_number": 9870898967675
        }
        self.user2 = {
            "username": "emmerson",
	        "email": "emayy@yahoo.com",
	        "firstname": "emma",
	        "lastname": "isabirye",
	        "othernames": "aaron",
	        "password": "gftdsjgg",
	        "phone_number": 9870898967675
        }      
        self.user3 = {
            "username": "dorothy",
            "email": "dora@gmail.com",
            "firstname": "dora",
            "lastname": "obbo",
            "othernames": "cata",
            "password": "12345",
            "phone_number": 8987767767
        }  
        self.user4 = {
            "username": "pius",
            "email": "pius@gmail.com",
            "firstname": "dora",
            "lastname": "obbo",
            "othernames": "cata",
            "password": "12345",
            "phone_number": 8987767767
        } 
        self.user5 = {
            "username": "peter",
            "email": "piusgmailcom",
            "firstname": "dora",
            "lastname": "obbo",
            "othernames": "cata",
            "password": "12345",
            "phone_number": 8987767767
        }   
        self.user6 = {
            "username": " ",
            "email": "pius@gmail.com",
            "firstname": "dora",
            "lastname": "obbo",
            "othernames": "cata",
            "password": "12345",
            "phone_number": 8987767767
        }   
        self.user7 = {
            "username": "mordecai",
            "email": "mordecai@gmail.com",
            "firstname": "dora",
            "lastname": "obbo",
            "othernames": "cata",
            "password": "12345",
            "phone_number": 8987767767
        }
        self.user_login = {
	        "email": "ema@yahoo.com",
	        "password": "gftdsjgg"
        }
        self.user_login2 = {
	        "email": "emayy@yahoo.com",
	        "password": "gftdsjgg"
        }        
        self.incidents = {
            "incident_type": "intervention",
            "location": "89887499.09, 9767787.90",
            "comment": "bocken bridge",
            "user_id": 1
        }
        self.incidents2 = {
            "incident_type": "",
            "location": "76767, 09088",
            "comment": " ",
            "user_id": 1
        }
        self.incidents3 = {
            "incident_type": "intervention",
            "location": "63767, 98979",
            "comment": "thefty",
            "user_id": 4534
        }
        self.incidents4 = {
            
        }
        self.signup_user(self.user)
        self.token = self.login_user(self.user_login)

    def signup_user(self, user):
        signedup_user = self.tester.post("api/v2/auth/signup",
         content_type="application/json", data=json.dumps(user))
        return signedup_user

    def login_user(self, user):
        loggedin_user = self.tester.post("api/v2/auth/login",
            content_type="application/json",
            data=json.dumps(user))
        token = json.loads(loggedin_user.data.decode())
        return token["data"][0]["token"]

    
    def tearDown(self):
        self.db.drop_tables()
