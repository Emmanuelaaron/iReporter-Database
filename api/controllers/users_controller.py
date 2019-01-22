from api.models.users_model import User
from flask import jsonify, request
from api.validation import Validating_string, email_validator
from db import Database_connection
import psycopg2

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
            user.signup(username, email, firstname, lastname, othernames, phone_number)
            return jsonify({
                "message": "user sucessfully registered"
            })
        except psycopg2.IntegrityError as e:
            e = "Email or username already taken!"
            return jsonify ({
                "message": e
            })

        # my_account = User(firstname, lastname, othernames, email, password, username)
        # my_account = my_account.signup()
        # my_account["users_id"] = len(users_list.get_all_users()) + 1
        # users_list.add_user(my_account)

        # return jsonify({
        #     "status": 201,
        #     "message": "You've signed up sucessfully!",
        #     "data": my_account
        # }), 201


