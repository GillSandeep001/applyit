class Command:
    def execute(self):
        pass


class AddApplicationCommand(Command):
    def __init__(self, db_func, app):
        self.db_func = db_func
        self.app = app

    def execute(self):
        self.db_func(self.app)


class UpdateStatusCommand(Command):
    def __init__(self, db_func, app_id, status):
        self.db_func = db_func
        self.app_id = app_id
        self.status = status

    def execute(self):
        self.db_func(self.app_id, self.status)