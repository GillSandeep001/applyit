class Command:
    """
    Base Command interface for the Command Design Pattern.

    This abstract class defines a common interface for all command objects.
    Each concrete command must implement the execute() method.
    """

    def execute(self):
        pass


class AddApplicationCommand(Command):
    """
    Concrete Command that handles adding a new job application.

    This class encapsulates the request to add an application
    and delegates the operation to the database layer.
    """

    def __init__(self, db_func, app):
        # Function reference to the database insert operation
        self.db_func = db_func

        # JobApplication object to be added
        self.app = app

    def execute(self):
        """
        Executes the command by calling the database function
        with the provided application object.
        """
        self.db_func(self.app)


class UpdateStatusCommand(Command):
    """
    Concrete Command that handles updating the status of an application.

    This class encapsulates the request to update an application's status
    and delegates the operation to the database layer.
    """

    def __init__(self, db_func, app_id, status):
        # Function reference to the database update operation
        self.db_func = db_func

        # ID of the application to be updated
        self.app_id = app_id

        # New status to be applied
        self.status = status

    def execute(self):
        """
        Executes the command by calling the database function
        with the application ID and new status.
        """
        self.db_func(self.app_id, self.status)