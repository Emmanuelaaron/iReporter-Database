import psycopg2
from pprint import pprint

class Database_connection():
    def __init__(self):
        try:
            self.connect = psycopg2.connect(dbname="ireporter", user="postgres", password='', host="127.0.0.1", port=5432)
            self.connect.autocommit = True
            self.cursor = self.connect.cursor()
            pprint("database running")
        except Exception as e:
            print(e)
            pprint("failed")
        self.create_tables()

    def create_tables(self):
        users_table = "CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY, username VARCHAR(50),\
                                                        email VARCHAR(50), firstname VARCHAR(50), \
                                                        lastname VARCHAR(50), othernames VARCHAR(50), \
                                                        phone_number INTENGER, isAdmin BOOLEAN);"
        self.cursor.execute(users_table)

        incidents_table = "CREATE TABLE IF NOT EXISTS incidents(incident_id SERIAL PRIMARY KEY, incident_type TEXT, \
                                                                createdOn TIMESTAMP DEFAULT NOW(), location, status TEXT,\
                                                                 comment TEXT, user_id INTEGER REFERENCES users);"

    


if __name__ == '__main__':
    db = Database_connection()