from db import Database, add_application, get_applications, update_status
from factory import ApplicationFactory
from command import AddApplicationCommand, UpdateStatusCommand
from state import ApplicationState
from api_service import get_company_info
from db import generate_report
import json


def menu():
    """
    Displays the main menu options to the user.

    This function represents the command-line interface (CLI) through which
    users interact with the ApplyIt system.
    """
    print("\n--- ApplyIt ---")
    print("1. Add Application")
    print("2. View Applications")
    print("3. Update Status")
    print("4. Fetch Company Info")
    print("5. Generate Report")
    print("6. Exit")


def main():
    """
    Main entry point of the ApplyIt application.

    This function acts as the controller of the system. It handles user input,
    coordinates interactions between different components (database, API,
    design pattern classes), and executes the appropriate operations.
    """

    # Initialize database connection
    db = Database()
    conn = db.get_connection()

    # Infinite loop to continuously accept user input
    while True:
        menu()
        choice = input("Enter choice: ")

        # Option 1: Add a new job application
        if choice == "1":
            company = input("Company: ")
            position = input("Position: ")
            status = input("Status: ")
            date = input("Date (YYYY-MM-DD): ")

            # Create application object using Factory Pattern
            app = ApplicationFactory.create_application(company, position, status, date)

            # Execute add operation using Command Pattern
            command = AddApplicationCommand(lambda a: add_application(conn, a), app)
            command.execute()

            print("Application added!")

        # Option 2: View all job applications
        elif choice == "2":
            apps = get_applications(conn)

            print("\nApplications:")
            for app in apps:
                print(app)

        # Option 3: Update application status
        elif choice == "3":
            app_id = input("Application ID: ")
            new_status = input("New Status: ")

            # Demonstrates State Pattern usage for status transition
            state = ApplicationState("old")
            state.change_status(new_status)

            # Execute update operation using Command Pattern
            command = UpdateStatusCommand(
                lambda i, s: update_status(conn, i, s),
                app_id,
                new_status
            )
            command.execute()

            print("Status updated!")

        # Option 4: Fetch company information from external API
        elif choice == "4":
            name = input("Enter company name: ")
            data = get_company_info(name)

            print("\nCompany Info:")

            # Display API response data
            if isinstance(data, list) and len(data) > 0:
                print("Company:", data[0].get("name"))
                print("Logo URL:", data[0].get("image"))
            else:
                print("No data found")

        # Option 5: Generate report from database
        elif choice == "5":
            total, status_counts = generate_report(conn)

            print("\n--- Job Application Report ---")
            print(f"Total Applications: {total}")

            print("\nApplications by Status:")
            for status, count in status_counts:
                print(f"{status}: {count}")

            print("\n--- End of Report ---")

        # Option 6: Exit application
        elif choice == "6":
            print("Exiting...")
            break

        # Handle invalid input
        else:
            print("Invalid choice")


# Program entry point
if __name__ == "__main__":
    main()