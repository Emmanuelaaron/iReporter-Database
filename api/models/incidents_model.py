import datetime
from db import Database_connection

class Incident:
    def __init__(self):
        self.database_obj = Database_connection()


    def create_incidence(self, incident_type, location, comment, user_id):
        incident = "INSERT INTO incidents(incident_type, location, status, comment, user_id)\
                    VALUES('{}', '{}', 'draft', '{}', {});".format(incident_type, location, comment, user_id)
        self.database_obj.cursor.execute(incident)

    def get_all_incidents(self):
        all_incidents = "SELECT * FROM incidents"
        self.database_obj.cursor.execute(all_incidents)
        incidents = self.database_obj.cursor.fetchall()
        return incidents

    def get_specific_incident(self, incident_id):
        incident = "SELECT * FROM incidents WHERE incident_id = '{}'".format(incident_id)
        self.database_obj.cursor.execute(incident)
        incident_ = self.database_obj.cursor.fetchone()
        return incident_
        
    def delete_specific_incident(self, incident_id):
        query = "DELETE FROM incidents WHERE incident_id = '{}'".format(incident_id)
        return self.database_obj.cursor.execute(query)
        
    def edit_comment_incident(self, incident_id, comment):
        query = "UPDATE incidents SET comment = '{}' \
                WHERE incident_id = '{}'".format(comment, incident_id)
        return self.database_obj.cursor.execute(query)
        
        