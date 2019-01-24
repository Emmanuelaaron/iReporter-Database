from api.models.users_model import User
from flask import jsonify, request
from api.validation import Validating_string, email_validator
from db import Database_connection
import psycopg2
from api.jwt_token import encode_auth_token

database_conn = Database_connection()
user = User()
class UsersController:

    @staticmethod
    def signupUser():
        data = request.get_json()
        firstname = data.get("firstname")
        lastname = data.get("lastname")
        othernames = data.get("othernames")
        email = data.get("email")
        password = data.get("password")
        username = data.get("username")
        phone_number = data.get("phone_number")

        if not email_validator.validate_email(email):
            return jsonify({
                "message": "Invalid email"
            }), 400
        user_details = [firstname, lastname, email, password, username]
        for detail in user_details:
            if Validating_string.is_space(detail) or not Validating_string.characters(detail):
                 return jsonify({
                     "status": 400,
                    "message": "All fields must be filled!"
                    }), 400
        try:
            user.signup(username, password, email, firstname, lastname, othernames, phone_number)
            token = encode_auth_token(email).decode("utf-8")
            return jsonify({
                "status": 201,
                "data": [{
                    "token": token,
                }]
            }), 201
        except psycopg2.IntegrityError as e:
            e = "Email or username already taken!"
            return jsonify ({
                "status": 400,
                "message": e
            }), 400

    @staticmethod
    def user_signin():
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        details = [email, password]
        for detail in details:
            if Validating_string.is_space(detail) or not Validating_string.characters(detail):
                    return jsonify({
                        "status": 400,
                        "message": "All fields must be filled!"
                        }), 400
        if database_conn.get_user(data):
            token = encode_auth_token(email).decode("utf-8")
            return jsonify({
                "status": 200,
                "data": [{
                    "token": token,
                    "message": "sucessfully logged in"
                }]
            }), 200
        return jsonify({
            "message": "invalid login credentials!",
            "status": 400
        }), 400
