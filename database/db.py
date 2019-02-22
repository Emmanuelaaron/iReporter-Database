import psycopg2
import psycopg2.extras
from pprint import pprint
import os


class Database_connection():

    def __init__(self):
           
        try:
            self.database_url = os.getenv("DATABASE_URL")

            self.connect = psycopg2.connect(self.database_url)
            self.connect.autocommit = True
            self.cursor = self.connect.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor)
            pprint("database running")
        except Exception as e:
            print(e)
            pprint("failed")
        self.create_tables()

    def create_tables(self):
        users_table = "CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY, username VARCHAR(50) UNIQUE,\
                        password VARCHAR(50), email VARCHAR(50) UNIQUE, firstname VARCHAR(50) NOT NULL,\
                        lastname VARCHAR(50) NULL, othernames VARCHAR(50) NULL,phone_number TEXT,\
                        registedOn TIMESTAMP DEFAULT NOW(), isAdmin BOOLEAN);"

        incidents_table = "CREATE TABLE IF NOT EXISTS incidents(incident_id SERIAL PRIMARY KEY,\
                            incident_type TEXT NOT NULL, createdOn TIMESTAMP DEFAULT NOW(), location TEXT,\
                            status TEXT, comment TEXT, user_id INTEGER REFERENCES users);"
                            
        self.cursor.execute(users_table)
        self.cursor.execute(incidents_table)
        


    def checker_captured(self, location, comment):
        query = """
            SELECT location, comment FROM incidents\
            WHERE location = '{}' AND comment = '{}'""".format(location, comment)
        self.cursor.execute(query)
        incident = self.cursor.fetchone()
        return incident

    def drop_tables(self):
        query = "DROP TABLE IF EXISTS {0} CASCADE"
        tables = ["users", "incidents"]
        for table in tables:
            self.cursor.execute(query.format(table))

    def get_user(self, login_details):
        query = "SELECT * FROM users WHERE email = '{}' AND password = \
                '{}';".format(login_details["email"], login_details["password"])
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result if True else False

    def in_data_base(self, incident_id):
        query = "SELECT * FROM incidents WHERE incident_id = '{}'".format(incident_id)
        self.cursor.execute(query)
        return self.cursor.fetchone()




if __name__ == '__main__':
    db = Database_connection()
