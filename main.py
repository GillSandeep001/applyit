from db import Database, add_application, get_applications, update_status
from factory import ApplicationFactory
from command import AddApplicationCommand, UpdateStatusCommand
from state import ApplicationState
from api_service import get_company_info
import json


def menu():
    print("\n--- ApplyIt ---")
    print("1. Add Application")
    print("2. View Applications")
    print("3. Update Status")
    print("4. Fetch Company Info")
    print("5. Exit")


def main():
    db = Database()
    conn = db.get_connection()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            company = input("Company: ")
            position = input("Position: ")
            status = input("Status: ")
            date = input("Date (YYYY-MM-DD): ")

            app = ApplicationFactory.create_application(company, position, status, date)

            
            command = AddApplicationCommand(lambda a: add_application(conn, a), app)
            command.execute()

            print("Application added!")

        elif choice == "2":
            apps = get_applications(conn)
            print("\nApplications:")
            for app in apps:
                print(app)

        elif choice == "3":
            app_id = input("Application ID: ")
            new_status = input("New Status: ")

            state = ApplicationState("old")
            state.change_status(new_status)

            command = UpdateStatusCommand(
                lambda i, s: update_status(conn, i, s),
                app_id,
                new_status
            )
            command.execute()

            print("Status updated!")

        elif choice == "4":
            name = input("Enter company name: ")
            data = get_company_info(name)

            print("\nCompany Info:")
            print(json.dumps(data, indent=2))

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()