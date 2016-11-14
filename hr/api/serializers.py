class EventMethod(object):
    CREATE = 'CREATE'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'


class InvalidEvent(Exception):
    pass


class EventlogPreconditionFailure(Exception):
    pass


class Event(object):
    def __init__(self, sequence, payload, method):
        # TODO  validate these parameters are legit
        self.sequence
        self.payload
        self.method


class EventLog(object):
    def publish():
        pass


class EventFactory(object):
    def __init__(self, validator):
        self.validator = validator

    def create(self, sequence, payload, method):
        self.validator.validate(sequence, payload, method)
        return Event(sequence, payload, method)


class ExpenseValidator(object):
    def validate():
        return True
