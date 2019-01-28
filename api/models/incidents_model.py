import datetime
from db import Database_connection

class Incident:
    def __init__(self):
        self.database_obj = Database_connection()


    def create_incidence(self, incident_type, location, comment, user_id):
        incident = "INSERT INTO incidents(incident_type, location, status, comment, user_id)\
                    VALUES('{}', '{}', 'draft', '{}', {});".format(incident_type, location, comment, user_id)
        self.database_obj.cursor.execute(incident)

    def get_all_interventions(self):
        all_interventions = "SELECT * FROM incidents WHERE incident_type = 'intervention'"
        self.database_obj.cursor.execute(all_interventions)
        incidents = self.database_obj.cursor.fetchall()
        return incidents

    def get_all_red_flags(self):
        all_red_flags = "SELECT * FROM incidents WHERE incident_type = 'red flag'"
        self.database_obj.cursor.execute(all_red_flags)
        incidents = self.database_obj.cursor.fetchall()
        return incidents

    def get_specific_intervention(self, incident_id):
        incident = "SELECT * FROM incidents WHERE incident_id = '{}'\
                     AND incident_type = 'intervention'".format(incident_id)
        self.database_obj.cursor.execute(incident)
        incident_ = self.database_obj.cursor.fetchone()
        return incident_

    def get_specific_red_flag(self, incident_id):
        incident = "SELECT * FROM incidents WHERE incident_id = '{}'\
                    AND incident_type = 'red flag'".format(incident_id)
        self.database_obj.cursor.execute(incident)
        incident_ = self.database_obj.cursor.fetchone()
        return incident_
        
    def delete_specific_intervention(self, incident_id):
        incident = "DELETE FROM incidents WHERE incident_id = '{}'\
                 AND incident_type = 'intervention'".format(incident_id)
        return self.database_obj.cursor.execute(incident)

    def delete_specific_red_flag(self, incident_id):
        incident = "DELETE FROM incidents WHERE incident_id = '{}'\
                    AND incident_type = 'red flag'".format(incident_id)
        return self.database_obj.cursor.execute(incident)
        
    def edit_comment_intervention(self, incident_id, comment):
        incident = "UPDATE incidents SET comment = '{}' \
                    WHERE incident_id = '{}' AND incident_type = 'intervention'".format(comment, incident_id)
        return self.database_obj.cursor.execute(incident)

    def edit_comment_red_flag(self, incident_id, comment):
        incident = "UPDATE incidents SET comment = '{}'\
                    WHERE incident_id = '{}' AND incident_type = 'red flag'".format(comment, incident_id)
        
        