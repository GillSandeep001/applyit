class JobApplication:
    """
    Represents a job application entity in the ApplyIt system.

    This class acts as the core data model used to store and manage
    job application details such as company name, position, status,
    and application date.
    """

    def __init__(self, company, position, status, date):
        # Name of the company applied to
        self.company = company

        # Job title or position applied for
        self.position = position

        # Current status of the application (e.g., Applied, Interview, Offer)
        self.status = status

        # Date when the application was submitted
        self.date = date

    def __str__(self):
        """
        Returns a formatted string representation of the job application.
        Used for displaying application details in the command-line interface.
        """
        return f"{self.company} | {self.position} | {self.status} | {self.date}"