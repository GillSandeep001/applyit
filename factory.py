from application import JobApplication

class ApplicationFactory:
    """
    Factory class implementing the Factory Design Pattern.

    This class is responsible for creating JobApplication objects.
    It encapsulates the object creation logic, allowing the rest of
    the system to remain independent of how objects are instantiated.
    """

    @staticmethod
    def create_application(company, position, status, date):
        """
        Creates and returns a new JobApplication object.

        Parameters:
        - company: name of the company
        - position: job position applied for
        - status: current application status
        - date: application date

        Returns:
        - JobApplication object
        """
        return JobApplication(company, position, status, date)