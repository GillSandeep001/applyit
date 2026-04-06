class JobApplication:
    def __init__(self, company, role, status, date):
        self.company = company
        self.role = role
        self.status = status
        self.date = date

    def __str__(self):
        return f"{self.company} | {self.role} | {self.status} | {self.date}"