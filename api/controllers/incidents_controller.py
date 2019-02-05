from api.models.incidents_model import Incident
from flask import jsonify, request
from api.validation import Validating_string
from database.db import Database_connection
import psycopg2

incident_obj = Incident()
database_conn = Database_connection()
class IncidentsController:

    def create_incidence(self):
        data = request.get_json()
        incident_type = data.get("incident_type")
        location = data.get("location")
        comment = data.get("comment")
        user_id = data.get("user_id")

        try:
            incidents_details = [incident_type, location, comment, user_id]
            for incident in incidents_details:
                if type(incident) is str:
                    if not Validating_string.characters(incident) or\
                    Validating_string.is_space(incident):
                        return jsonify({
                            "status": 400,
                            "error": "All fields must be filled!"
                            }), 400
            checker = database_conn.checker_captured(location, comment)
            if checker:
                return jsonify({
                    "status": 200,
                    "data": "already captured!"
                }), 200

            try:
                incident_obj.create_incidence(incident_type, location, comment, user_id)
                return jsonify({
                    "status": 201,
                    "data": [{
                        "message": "created incident record" 
                    }]
                }), 201
            except psycopg2.IntegrityError as e:
                e = "user_id does not exist!"
                return jsonify({
                    "status": 401,
                    "error": e
                }), 401
        except psycopg2.ProgrammingError as e:
            e = "Oops fields not filled!"
            return jsonify({
                "status": 401,
                "error": e
            }), 401
            
    def get_interventions(self):
        incidents_ = incident_obj.get_all_interventions()
        return jsonify({
            "status": 200,
            "data": [incidents_]
        }), 200

    def get_red_flags(self):
        incidents = incident_obj.get_all_red_flags()
        return jsonify({
            "status": 200,
            "data": [incidents]
        }), 200

    def get_specific_intervention(self, incident_id):
        incidence = incident_obj.get_specific_intervention(incident_id)
        if incidence:
            return jsonify({
                    "status": 200,
                    "data": [incidence]
                }), 200
        return jsonify({
            "status": 400,
            "error": "incident_id does not exist"
        }), 400

    def get_specific_red_flag(self, incident_id):
        incidence = incident_obj.get_specific_red_flag(incident_id)
        if incidence:
            return jsonify({
                "status": 200,
                "data": [incidence]
            }), 200
        return jsonify({
            "status": 400,
            "error": "incident_id does not exist"
        }), 400

    def delete_specific_intervention(self, incident_id):
        if not database_conn.in_data_base(incident_id):
            return jsonify({
                "status": 400,
                "error": "incident_id does not exist!"
            }), 400
        incident_obj.delete_specific_intervention(incident_id)
        return jsonify({
            "status": 200,
            "data": [{
                "id": incident_id,
                "message": "intervetion record has been deleted"
            }]
        })

    def delete_specific_red_flag(self, incident_id):
        if not database_conn.in_data_base(incident_id):
            return jsonify({
                "status": 400,
                "error": "incident_id does not exist!"
            }), 400
        incident_obj.delete_specific_red_flag(incident_id)
        return jsonify({
            "status": 200,
            "data": [{
                "id": incident_id,
                "message": "red flag record has been deleted"
            }]
        }), 200

    def edit_comment_specific_intervention(self, incident_id):
        data = request.get_json()
        comment = data.get("comment")
        incident_obj.edit_comment_intervention(incident_id, comment)
        return jsonify({
            "status": 200,
            "data": [{
                "id": incident_id,
                "message": "updated intervention's record comment"
            }]
        }), 200

    def edit_comment_specific_red_flag(self, incident_id):
        data = request.get_json()
        comment = data.get("comment")
        incident_obj.edit_comment_red_flag(incident_id, comment)
        return jsonify({
            "status": 200,
            "data": [{
                "id": incident_id,
                "message": "Updated red flag's record comment"
            }]
        })