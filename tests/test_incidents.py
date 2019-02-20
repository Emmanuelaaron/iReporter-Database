import unittest
from api import app
from flask import json
from tests.base_test import BaseTest 

class TestIncidents(BaseTest):

    def test_create_incidence(self):
        resp = self.tester.post(
            "api/v2/incidence",
            headers={
                "x-access-token": self.token
            },
            content_type="application/json",
            data=json.dumps(self.incidents)
        )
        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 201)
        self.assertEqual(reply["data"][0]["message"], "created incident record")
    
    def test_create_incidence_already_captured(self):
#This function tests when the same incidence is being created!
        resp = self.tester.post("api/v2/incidence", 
                headers={"x-access-token": self.token},
                content_type="application/json",
                data=json.dumps(self.incidents)
        )
        resp = self.tester.post("api/v2/incidence", 
                headers={"x-access-token": self.token},
                content_type="application/json",
                data=json.dumps(self.incidents)
        )
        reply = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(reply["data"], "already captured!")
    
    def test_create_incidence_empty_fieled(self):
        resp = self.tester.post("api/v2/incidence", 
                headers={"x-access-token": self.token},
                content_type="application/json",
                data=json.dumps(self.incidents2)
        )
        reply = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(reply["error"], "All fields must be filled!")
    
    def test_create_incidence_invalid_user_id(self):
        resp = self.tester.post("api/v2/incidence", 
                headers={"x-access-token": self.token},
                content_type="application/json",
                data=json.dumps(self.incidents3)
        )
        reply = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(reply["error"], "user_id does not exist!")

    def test_create_incidence_invalid_json(self):
        resp = self.tester.post("api/v2/incidence", 
                headers={"x-access-token": self.token},
                content_type="application/json",
                data=json.dumps(self.incidents4)
        )
        reply = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(reply["error"], "Oops something went wrong!")



    def test_get_all_interventions(self):
        resp = self.tester.get(
            "api/v2/interventions",
            headers={
                "x-access-token": self.token
            },
        )
        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(reply)

    def test_get_all_interventions_invalid_token(self):
        resp = self.tester.get(
            "api/v2/interventions",
            headers={
                "x-access-token": self.incidents
            }
        )
        reply = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 401)

#when the token is missing
    def test_get_all_interventions_token_missing(self):
        resp = self.tester.get(
            "api/v2/interventions"
        )
        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 401)
        self.assertEqual(reply["error"], "token missing")

    def test_get_red_flags(self):
        resp = app.test_client(self).get(
            "api/v2/red-flags",
            headers={
                "x-access-token": self.token
            },
        )
        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(reply)

    def test_get_specific_intervention(self):
        resp = self.tester.get(
            "api/v2/interventions/1",
            headers={
                "x-access-token": self.token
            },
        )
        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 400)
        self.assertEqual(reply["error"], "incident_id does not exist")


    def test_get_specific_red_flag(self):
        resp = self.tester.get(
            "api/v2/red-flags/1",
            headers={
                "x-access-token": self.token
            },
        )
        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 400)
        self.assertEqual(reply["error"], "incident_id does not exist")

    def test_delete_specific_intervention_no_incidence(self):
        resp = self.tester.delete(
            "api/v2/interventions/1",
            headers={
                "x-access-token": self.token
            },
        )
        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 400)
        self.assertEqual(reply["error"], "incident_id does not exist!")

    def test_delete_specific_red_flag_no_incidennt(self):
        resp = self.tester.delete(
            "api/v2/red-flags/1",
            headers={
                "x-access-token": self.token
            },
        )
        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 400)
        self.assertEqual(reply["error"], "incident_id does not exist!")

    def test_delete_specific_intervention(self):

        resp = app.test_client(self).post(
            "api/v2/incidence",
            headers={
                "x-access-token": self.token
            },
            content_type="application/json",
            data=json.dumps(self.incidents)
        )

        resp = app.test_client(self).delete(
            "api/v2/interventions/1",
            headers={
                "x-access-token": self.token
            },
        )
        reply = json.loads(resp.data.decode())

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(reply["data"][0]["message"], "intervetion record has been deleted")




