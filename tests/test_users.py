import unittest
from api import app
from flask import json
from tests.base_test import BaseTest

class TestUser(BaseTest):

    def test_signupuser(self):

        resp = app.test_client(self).post(
            "api/v2/signup", 
            content_type="application/json",
            data=json.dumps(self.user)
        )

        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 201)
        self.assertEqual(reply["message"], "You've signed up sucessfully!")
        self.assertIn("You've signed up sucessfully!", str(reply))


    def test_signin(self):
        resp = app.test_client(self).post(
            "api/v2/signup", 
            content_type="application/json",
            data=json.dumps(self.user)
        )
        resp = app.test_client(self).post(
            "api/v2/login",
            content_type="application/json",
            data=json.dumps({
                "email": "ema@yahoo.com",
                "password": "gftdsjgg"
            })
        )

        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(reply["message"], "sucessfully loggedin")
