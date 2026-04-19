import psycopg2
import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()


class Database:
    """
    Handles database connection setup for the ApplyIt system.

    This class is responsible for establishing a connection to the PostgreSQL
    database using credentials stored securely in environment variables.
    """

    def __init__(self):
        # Establish connection to PostgreSQL database
        self.connection = psycopg2.connect(
            host="localhost",
            database="applyit",
            user="postgres",
            password=os.getenv("DB_PASSWORD")  # Securely load password from environment variable
        )

    def get_connection(self):
        """
        Returns the active database connection.
        """
        return self.connection


def add_application(conn, app):
    """
    Inserts a new job application record into the database.

    Parameters:
    - conn: active database connection
    - app: JobApplication object containing application details
    """
    cursor = conn.cursor()

    # Execute SQL insert query
    cursor.execute(
        "INSERT INTO job_applications (company, position, status) VALUES (%s,%s,%s)",
        (app.company, app.position, app.status)
    )

    # Commit changes to the database
    conn.commit()
    cursor.close()


def get_applications(conn):
    """
    Retrieves all job application records from the database.

    Returns:
    - List of all application records
    """
    cursor = conn.cursor()

    # Execute SQL select query
    cursor.execute("SELECT * FROM job_applications")

    rows = cursor.fetchall()
    cursor.close()

    return rows


def update_status(conn, app_id, status):
    """
    Updates the status of a specific job application.

    Parameters:
    - conn: active database connection
    - app_id: ID of the application to update
    - status: new status value
    """
    cursor = conn.cursor()

    # Execute SQL update query
    cursor.execute(
        "UPDATE job_applications SET status = %s WHERE id = %s",
        (status, app_id)
    )

    conn.commit()
    cursor.close()


def generate_report(conn):
    """
    Generates a summary report of job applications.

    Returns:
    - total: total number of applications
    - status_counts: number of applications grouped by status
    """
    cursor = conn.cursor()

    # Get total number of applications
    cursor.execute("SELECT COUNT(*) FROM job_applications")
    total = cursor.fetchone()[0]

    # Get count of applications grouped by status
    cursor.execute("""
        SELECT status, COUNT(*)
        FROM job_applications
        GROUP BY status
    """)
    status_counts = cursor.fetchall()

    cursor.close()

    return total, status_counts