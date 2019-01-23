from flask import Blueprint
from api.controllers.incidents_controller import IncidentsController


incidence = IncidentsController()
incidents_blueprint = Blueprint("incidents", __name__, url_prefix="/api/v2")

@incidents_blueprint.route("/red-flags", methods=["POST"])
def create_incident():
    return incidence.create_incidence()

@incidents_blueprint.route("/red-flags")
def get_all_incidents():
    return IncidentsController.get_incidents()

@incidents_blueprint.route("/red-flags/<int:incident_id>")
def get_specific_incident(incident_id):
    return IncidentsController.get_specific_incident(incident_id)

@incidents_blueprint.route("/red-flags/<int:incident_id>", methods=["DELETE"])
def delete_specific_red_flag(incident_id):
    return incidence.delete_specific_incident(incident_id)

@incidents_blueprint.route("/red-flags/<incident_id>/comment", methods=["PATCH"])
def edit_comment_specific_incident(incident_id):
    return incidence.edit_comment_specific_incident(incident_id)




