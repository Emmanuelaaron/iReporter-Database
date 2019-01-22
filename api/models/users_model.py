from db import Database_connection

class User():
    def __init__(self):
        self.database_obj = Database_connection()

    def signup(self, username, email, firstname, lastname, othernames, phone_number):
        # isAdmin = False
        user = "INSERT INTO users(username, email, firstname, lastname, othernames, phone_number)\
                VALUES ('{}', '{}', '{}', '{}', '{}', '{}');".format(username, email, firstname, lastname, othernames, phone_number)
        self.database_obj.cursor.execute(user)

