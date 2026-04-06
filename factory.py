from application import JobApplication

class ApplicationFactory:
    @staticmethod
    def create_application(company, position, status):
        return JobApplication(company, position, status)