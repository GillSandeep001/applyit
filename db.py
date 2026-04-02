import psycopg2

class Database:

    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            database="applyit",
            user="postgres",
            password="GillSaab683"
        )

    def get_connection(self):
        return self.connection