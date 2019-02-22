from database.db import Database_connection

class User():
    def __init__(self):
        self.database_obj = Database_connection()

    def signup(self, username, password, email, firstname, lastname, othernames, phone_number):
        isAdmin = False
        user = "INSERT INTO users(username, password, email, firstname, lastname, othernames, phone_number, isAdmin)\
                VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(username, password, email, firstname, lastname, othernames, phone_number, isAdmin)
        self.database_obj.cursor.execute(user)
    


