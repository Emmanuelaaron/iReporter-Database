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
        # self.assertEqual(reply["data"]['email'], 'ema@yahoo.com')
    #     self.assertEqual(reply["data"]["lastname"], "ngiya")
    #     self.assertEqual(reply["data"]["username"], "dojo")
    #     self.assertEqual(reply["data"]["firstname"], "Donald")
    #     self.assertEqual(resp.status_code, 201)

    # def test_signupuser_without_a_field(self):
    #     user = dict(
    #         firstname="",
    #         lastname="ngiya",
    #         othernames="Danny",
    #         email="ngiya@gams.com",
    #         password="ghgdhgd",
    #         username="dojo"
    #     )
    #     resp = app.test_client(self).post(
    #         "api/v1/signup",
    #         content_type="application/json",
    #         data = json.dumps(user)
    #     )

    #     reply = json.loads(resp.data.decode())

    #     self.assertEqual(reply["message"], "All fields must be filled!")
    #     self.assertEqual(resp.status_code, 400)

    # def test_more_tests(self):
    #     resp = app.test_client(self).get(
    #         "api/v1"
    #     )
    #     self.assertEqual(resp.status_code, 301)
