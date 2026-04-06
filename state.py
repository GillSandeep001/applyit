class ApplicationState:
    def __init__(self, status):
        self.status = status

    def change_status(self, new_status):
        print(f"Changing status from {self.status} → {new_status}")
        self.status = new_status