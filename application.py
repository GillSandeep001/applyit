class JobApplication:

    def __init__(self, company, position, status):
        self.company = company
        self.position = position
        self.status = status

    def __str__(self):
        return f"{self.company} - {self.position} ({self.status})"