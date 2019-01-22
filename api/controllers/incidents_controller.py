from api.models.incidents_model import Incident
from flask import jsonify, request
from api.validation import Validating_string
from db import Database_connection
import psycopg2

incident_obj = Incident()
database_conn = Database_connection()
class IncidentsController:

    @staticmethod
    def create_incidence():
        data = request.get_json()
        incident_type = data.get("incident_type")
        location = data.get("location")
        comment = data.get("comment")
        user_id = data.get("user_id")

        incidents_details = [incident_type, location, comment, user_id]
        for incident in incidents_details:
            if type(incident) is str:
                if not Validating_string.characters(incident) or\
                Validating_string.is_space(incident):
                    return jsonify({
                        "status": 400,
                        "message": "All fields must be filled!"
                        }), 400
        checker = database_conn.checker_captured(location, comment)
        if checker:
            return jsonify({
                "message": "already captured!"
            })

        try:
            incident_obj.create_incidence(incident_type, location, comment, user_id)
            return jsonify({
                "message": "sucessfully created an incidence"
            })
        except psycopg2.IntegrityError as e:
            e = "user_id does not exist!"
            return jsonify({
                "message": e
            })

    @staticmethod
    def get_incidents():
        incidents_ = incident_obj.get_all_incidents()
        return jsonify({
            "message": incidents_
        })

    @staticmethod
    def get_specific_incident(incident_id):
        incidence = incident_obj.get_specific_incident(incident_id)
        if incidence:
            return jsonify({
                    "message": incidence
                })
        return jsonify({
            "message": "incident_id does not exist"
        })
    # @staticmethod
    # def delete_specific_red_flag(flag_id):
    #     if not Validating_string.characters(incidents_list.get_all_incidents()):
    #         return jsonify({
    #             "message": "No incidents!",
    #             "status": 400
    #         }), 400
    #     for incident in incidents_list.get_all_incidents():
    #         if incident["id"] != flag_id:
    #             return jsonify({
    #                 "message": "Flag id does not exist!"
    #             }), 400
    #         incidents_list.get_all_incidents().remove(incident)
    #         return jsonify({
    #             "message": "Sucessfully deleted!"
    #         }), 200

    # @staticmethod
    # def edit_comment_specific_red_flag(flag_id):
    #     if not Validating_string.characters(incidents_list.get_all_incidents()):
    #         return jsonify({
    #             "message": "No incidents!",
    #             "status": 400
    #         }), 400
    #     for incident in incidents_list.get_all_incidents():
    #         if incident["id"] != flag_id:
    #             return jsonify({
    #                 "message": "Flag id does not exist!"
    #             }), 400
    #         comment = request.get_json().get("comment")
    #         new_comment = comment
    #         incident["comment"] = new_comment
    #         return jsonify({
    #             "message": "You've sucessfully edited the comment!"
    #         }), 200

    # @staticmethod
    # def edit_location_specific_red_flag(flag_id):
    #     if not len(incidents_list.get_all_incidents() > 1):
    #         return jsonify({
    #             "message": "No incidents!",
    #             "status": 400
    #         }), 400
    #     for incident in incidents_list.get_all_incidents():
    #         if incident["id"] != flag_id:
    #             return jsonify({
    #                 "message": "Flag id does not exist!"
    #             }), 400
    #         print (incident["location"])
    #         location = request.get_json().get("location")
    #         new_location = location
    #         incident["location"] = new_location
    #         return jsonify({
    #             "message": "You've sucessfully edited the comment!"
    #         }), 200 