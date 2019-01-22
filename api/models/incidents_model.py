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
        