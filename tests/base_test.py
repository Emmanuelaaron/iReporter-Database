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
        self.incidents = {
            "incident_type": "intervention",
            "location": "89887499.09, 9767787.90",
            "comment": "bocken bridge",
            "user_id": 1
        }
    
    def tearDown(self):
        self.db.drop_tables()
