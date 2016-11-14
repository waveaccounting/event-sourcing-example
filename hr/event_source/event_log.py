class Event(object):
    def __init__(self, sequence,  method, payload):
        # TODO  validate these parameters are legit
        self.method = method
        self.payload = payload
        self.sequence = sequence


class EventFactory(object):
    def __init__(self, validator):
        self.validator = validator

    def create(self, sequence, payload, method):
        self.validator.validate(sequence, payload, method)
        return Event(sequence, payload, method)


class EventLog(object):
    def __init__(self, model):
        self.model = model

    def publish(self, event):
        # ensure crud is legit (state machine is able to C/U/D)
        # Write to db
        pass
