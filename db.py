import psycopg2
import psycopg2.extras
from pprint import pprint
import os


class Database_connection():

    def __init__(self):
        if os.getenv("DATABASE_NAME") == "ireporter_test":
            self.database_name = "ireporter_test"
            self.user="postgres"
            self.password='' 
            self.host="127.0.0.1" 
        else:
            self.database_name = "dckqjk91f93li1"
            self.user="brlyrkevgtzemb"
            self.password="0de57d06e656d1197989d386fa8e6ce69be56b0e8d7fcbe9d21918a33c70cb4f" 
            self.host="ec2-54-227-246-152.compute-1.amazonaws.com"
        print(self.database_name)
        try:
            self.connect = psycopg2.connect(
                dbname=self.database_name, user=self.user, password=self.password, host=self.host, port=5432)
            self.connect.autocommit = True
            self.cursor = self.connect.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor)
            pprint("database running")
        except Exception as e:
            print(e)
            pprint("failed")
        self.create_tables()

    def create_tables(self):
        users_table = "CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY, username VARCHAR(50) UNIQUE , password VARCHAR(50),\
                                                        email VARCHAR(50) UNIQUE, firstname VARCHAR(50) NOT NULL,\
                                                        lastname VARCHAR(50) NULL, othernames VARCHAR(50) NULL,\
                                                        phone_number TEXT);"
        incidents_table = "CREATE TABLE IF NOT EXISTS incidents(incident_id SERIAL PRIMARY KEY, incident_type TEXT NOT NULL, \
                                                                createdOn TIMESTAMP DEFAULT NOW(), location TEXT, status TEXT,\
                                                                 comment TEXT, user_id INTEGER REFERENCES users);"
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
