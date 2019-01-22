from flask import Blueprint
from api.controllers.incidents_controller import IncidentsController


incidence = IncidentsController()
incidents_blueprint = Blueprint("incidents", __name__, url_prefix="/api/v2")

@incidents_blueprint.route("/red-flags", methods=["POST"])
def create_incident():
    return incidence.create_incidence()