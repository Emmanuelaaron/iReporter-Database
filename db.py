import psycopg2
import psycopg2.extras
from pprint import pprint

class Database_connection():
    def __init__(self):
        try:
            self.connect = psycopg2.connect(dbname="ireporter", user="postgres", password='', host="127.0.0.1", port=5432)
            self.connect.autocommit = True
            self.cursor = self.connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            pprint("database running")
        except Exception as e:
            print(e)
            pprint("failed")
        self.create_tables()

    def create_tables(self):
        users_table = "CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY, username VARCHAR(50) UNIQUE ,\
                                                        email VARCHAR(50) UNIQUE, firstname VARCHAR(50) NOT NULL,\
                                                        lastname VARCHAR(50) NULL, othernames VARCHAR(50) NULL,\
                                                        phone_number TEXT);"
        return(self.cursor.execute(users_table))
            
        

        incidents_table = "CREATE TABLE IF NOT EXISTS incidents(incident_id SERIAL PRIMARY KEY, incident_type TEXT NOT NULL, \
                                                                createdOn TIMESTAMP DEFAULT NOW(), location TEXT, status TEXT,\
                                                                 comment TEXT, user_id INTEGER REFERENCES users);"
        self.cursor.execute(incidents_table)

    def check_username(self, username):
        query = "SELECT username FROM users WHERE username = '{}'".format(username)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user
    
    def check_email(self, email):
        query = "SELECT email * FROM users WHERE email = '{}'".format(email)
        self.cursor.execute(query)
        email = self.cursor.fetchone()
        return email

    # def check_unique():
    #     query = "SELECT * FROM users WHERE "
    
    


if __name__ == '__main__':
    db = Database_connection()