import unittest
from api import app
from flask import json
from db import Database_connection

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
    
    def tearDown(self):
        self.db.drop_tables()
