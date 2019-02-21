import unittest
from api import app
from flask import json
from tests.base_test import BaseTest

class TestUser(BaseTest):

    def test_signupuser(self):
        resp = self.signup_user(self.user2)
        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 201)
        self.assertIn("You've signed up sucessfully!", str(reply))

    def test_signupuser_user_already_exists(self):
        resp = self.signup_user(self.user4)
        resp = self.signup_user(self.user4)
        reply = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 400)
        self.assertIn("Email or username already taken!", str(reply))

    def test_signupuser_with_invalid_email(self):
        resp = self.signup_user(self.user5)
        reply = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(reply["message"], "Invalid email")

    def test_signupuser_with_empty_fieled(self):
        resp = self.signup_user(self.user6)
        reply = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(reply["message"], "All fields must be filled!")

    def test_signupuser_with_invalid_json(self):
        resp = self.signup_user(self.incidents4)
        reply = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(reply["message"], "Oops something went wrong!")

    def test_signin(self):
        resp = self.signup_user(self.user3)
        resp = app.test_client(self).post(
            "api/v2/auth/login",
            content_type="application/json",
            data=json.dumps({
                "email": "dora@gmail.com",
                "password": "12345"
            })
        )

        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 200)
        self.assertIn("sucessfully logged in", str(reply))

    def test_signin_with_Wrong_login_credentials(self):
        resp = self.signup_user(self.user6)
        resp = app.test_client(self).post(
            "api/v2/auth/login",
            content_type="application/json",
            data=json.dumps({
                "email": "dora@gmail.com",
                "password": "1234tyt5"
            })
        )

        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 400)
        self.assertEqual(reply["message"], "invalid login credentials!")

    def test_signin_with_With_invalid_json(self):
        resp = self.signup_user(self.user7)
        resp = app.test_client(self).post(
            "api/v2/auth/login",
            content_type="application/json",
            data=json.dumps({
               
            })
        )

        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 400)
        self.assertEqual(reply["message"], "Oops something went wrong!")
