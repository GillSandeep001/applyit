class JobApplication:
        def __init__(self, company, position, status, date):
            self.company = company
            self.position = position
            self.status = status
            self.date = date
        def __str__(self):
            return f"{self.company} | {self.position} | {self.status} | {self.date}"