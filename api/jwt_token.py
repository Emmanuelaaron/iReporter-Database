import jwt
import datetime
from functools import wraps
from flask import request, jsonify
from database.db import Database_connection

database_conn = Database_connection()
def encode_auth_token(email):

    try:
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=1800),
            "iat": datetime.datetime.utcnow(),
            "email": email
        }
        return jwt.encode(
            payload,
            "coding is cool"
        )
    except Exception as e:
        return e



# def get_user(username):
#     query = "SELECT  * FROM users WHERE username = '{}' RETURNING username".format(username)
#     database_conn.cursor.execute(query)

    