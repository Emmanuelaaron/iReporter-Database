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

    def test_get_all_interventions(self):
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
        resp = app.test_client(self).get(
            "api/v2/interventions",
            headers={
                "x-access-token": token["data"][0]["token"]
            },
        )
        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(reply)

#when the token is missing
    def test_get_all_interventions_token_missing(self):
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
        resp = app.test_client(self).get(
            "api/v2/interventions"
        )
        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 401)
        self.assertEqual(reply["error"], "token missing")

    def test_get_red_flags(self):
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
        resp = app.test_client(self).get(
            "api/v2/red-flags",
            headers={
                "x-access-token": token["data"][0]["token"]
            },
        )
        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(reply)

    def test_get_specific_intervention(self):
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
        resp = app.test_client(self).get(
            "api/v2/interventions/1",
            headers={
                "x-access-token": token["data"][0]["token"]
            },
        )
        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 400)
        self.assertEqual(reply["error"], "incident_id does not exist")


    def test_get_specific_red_flag(self):
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
        resp = app.test_client(self).get(
            "api/v2/red-flags/1",
            headers={
                "x-access-token": token["data"][0]["token"]
            },
        )
        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 400)
        self.assertEqual(reply["error"], "incident_id does not exist")

    def test_delete_specific_intervention_no_incidence(self):
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
        resp = app.test_client(self).delete(
            "api/v2/interventions/1",
            headers={
                "x-access-token": token["data"][0]["token"]
            },
        )
        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 400)
        self.assertEqual(reply["error"], "incident_id does not exist!")

    def test_delete_specific_red_flag_no_incidennt(self):
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
        resp = app.test_client(self).delete(
            "api/v2/red-flags/1",
            headers={
                "x-access-token": token["data"][0]["token"]
            },
        )
        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 400)
        self.assertEqual(reply["error"], "incident_id does not exist!")

    def test_delete_specific_intervention(self):
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

        resp = app.test_client(self).delete(
            "api/v2/interventions/1",
            headers={
                "x-access-token": token["data"][0]["token"]
            },
        )
        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 200)
        # self.assertEqual(reply["error"], "incident_id does not exist!")




