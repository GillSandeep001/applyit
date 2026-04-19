class ApplicationState:
    """
    Represents the state of a job application in the ApplyIt system.

    This class is used to manage and track the current status of a job
    application (e.g., Applied, Interview, Offer). It demonstrates a
    simplified implementation of the State Design Pattern by allowing
    the status of an application to change dynamically at runtime.
    """

    def __init__(self, status):
        # Current state (status) of the application
        self.status = status

    def change_status(self, new_status):
        """
        Updates the current state of the application.

        Parameters:
        - new_status: the new status to transition to

        This method simulates a state transition by updating the
        application status and printing the change.
        """
        print(f"Changing status from {self.status} → {new_status}")
        self.status = new_status