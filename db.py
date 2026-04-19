import psycopg2
import os

import dotenv

dotenv.load_dotenv()


  
class Database:

    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            database="applyit",
            user="postgres",
            password = os.getenv("DB_PASSWORD")
        )

    def get_connection(self):
        return self.connection


def add_application(conn, app):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO job_applications (company, position, status) VALUES (%s,%s,%s)",
        (app.company, app.position, app.status)
    )
    conn.commit()
    cursor.close()


def get_applications(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM job_applications")
    rows = cursor.fetchall()
    cursor.close()
    return rows


def update_status(conn, app_id, status):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE job_applications SET status = %s WHERE id = %s",
        (status, app_id)
    )
    conn.commit()
    cursor.close()

def generate_report(conn):
    cursor = conn.cursor()

    # Total applications
    cursor.execute("SELECT COUNT(*) FROM job_applications")
    total = cursor.fetchone()[0]

    # Count by status
    cursor.execute("""
        SELECT status, COUNT(*)
        FROM job_applications
        GROUP BY status
    """)
    status_counts = cursor.fetchall()

    cursor.close()

    return total, status_counts