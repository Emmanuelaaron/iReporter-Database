# import unittest
# from api import app
# from flask import json
# from tests.base_test import BaseTest

# class TestIncidents(BaseTest):

#     def test_create_incidence(self):
#         res = app.test_client(self).post(
#             "api/v2/signup", 
#             content_type="application/json",
#             data=json.dumps(self.user)
#         )
#         respo = app.test_client(self).post(
#             "api/v2/login",
#             content_type="application/json",
#             data=json.dumps({
#                 "email": "ema@yahoo.com",
#                 "password": "gftdsjgg"
#             })
#         )
#         token = json.loads(respo.data.decode())
#         resp = app.test_client(self).post(
#             "api/v2/red-flags",
#             # headers = {
#             #     "x-access-token": token["token"]
#             # },
#             content_type="application",
#             data=json.dumps(self.incidents)
#         )

#         self.assertEqual(resp.status_code, 201)