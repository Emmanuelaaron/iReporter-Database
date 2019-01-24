from flask import Blueprint
from api.controllers.users_controller import UsersController

my_user = UsersController()
users_blueprint = Blueprint("users", __name__, url_prefix="/api/v2")

@users_blueprint.route("/")
def index():
    return "welcome to ireporter"

@users_blueprint.route("/auth/signup", methods=["POST"])
def signup_user():
    return my_user.signupUser()

@users_blueprint.route("/auth/login", methods=["POST"])
def signin_user():
    return my_user.user_signin()