import unittest
from api import app
from flask import json
from tests.base_test import BaseTest

class TestIncidents(BaseTest):

    def test_create_incidence(self):
        resp = app.test_client(self).post(
            "api/v2/auth/signup", 
            content_type="application/json",
            data=json.dumps(self.user)
        )
        resp = app.test_client(self).post(
            "api/v2/auth/login",
            content_type="application/json",
            data=json.dumps({
                "email": "ema@yahoo.com",
                "password": "gftdsjgg"
            })
        )
        token = json.loads(resp.data.decode())
        resp = app.test_client(self).post(
            "api/v2/incidence",
            headers={
                "x-access-token": token["data"][0]["token"]
            },
            content_type="application/json",
            data=json.dumps(self.incidents)
        )
        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 201)
        self.assertEqual(reply["data"][0]["message"], "created intervention record")