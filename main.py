from db import Database
from application import JobApplication
from api_service import get_company_info
import json


def add_application(conn, application):

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO job_applications (company, position, status) VALUES (%s,%s,%s)",
        (application.company, application.position, application.status)
    )

    conn.commit()
    cursor.close()


def show_applications(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM job_applications")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()



def main():

    db = Database()
    conn = db.get_connection()

    app = JobApplication("Google", "Software Engineer", "Applied")

    add_application(conn, app)

    print("Applications in database:")

    show_applications(conn)

    print("\nFetching company info...\n")

    data = get_company_info("Google")

    print("Raw API Response:")
    print(data)

    print("\nFormatted Response:")
    print(json.dumps(data, indent=2))

    


if __name__ == "__main__":
    main()