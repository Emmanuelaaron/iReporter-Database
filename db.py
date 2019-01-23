import psycopg2
import psycopg2.extras
from pprint import pprint
import os

class Database_connection():

    def __init__(self):
        if os.getenv("DATABASE_NAME")=="ireporter_test":
            self.database_name = "ireporter_test"
        else:
            self.database_name = "ireporter"
        print (self.database_name)
        try:
            self.connect = psycopg2.connect(dbname=self.database_name, user="postgres", password='', host="127.0.0.1", port=5432)
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

    def checker_captured(self, location, comment):
        query = """
            SELECT location, comment FROM incidents\
            WHERE location = '{}' AND comment = '{}'""".format(location, comment)
        self.cursor.execute(query)
        incident = self.cursor.fetchone()
        return incident

    def drop_tables(self):
        query = "DROP TABLE IF EXISTS {0} CASCADE"
        tables = ["users"]
        for table in tables:
            self.cursor.execute(query.format(table))


if __name__ == '__main__':
    db = Database_connection()