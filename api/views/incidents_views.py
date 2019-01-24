from flask import Blueprint, request, jsonify
from api.controllers.incidents_controller import IncidentsController
from functools import wraps
import jwt
from api import app
incidence = IncidentsController()
incidents_blueprint = Blueprint("incidents", __name__, url_prefix="/api/v2")

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({
                "message": "token missing"
            })
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
            user_email = data["email"]
        except:
            return jsonify({
                "message": "invalid token!"
            })
        return f(user_email, *args, **kwargs)
    return decorated


@incidents_blueprint.route("/red-flags", methods=["POST"])
@token_required
def create_incident(user_email):
    return incidence.create_incidence()

@incidents_blueprint.route("/red-flags")
@token_required
def get_all_incidents(user_email):
    return IncidentsController.get_incidents()


@incidents_blueprint.route("/red-flags/<int:incident_id>")
# @token_required
def get_specific_incident(user_email, incident_id):
    return IncidentsController.get_specific_incident(incident_id)

@incidents_blueprint.route("/red-flags/<int:incident_id>", methods=["DELETE"])
@token_required
def delete_specific_red_flag(user_email, incident_id):
    return incidence.delete_specific_incident(incident_id)

@incidents_blueprint.route("/red-flags/<incident_id>/comment", methods=["PATCH"])
@token_required
def edit_comment_specific_incident(user_email, incident_id):
    return incidence.edit_comment_specific_incident(incident_id)




