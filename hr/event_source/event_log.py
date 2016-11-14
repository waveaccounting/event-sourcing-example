class Event(object):
    def __init__(self, sequence,  method, payload, modelName):
        # TODO  validate these parameters are legit
        self.method = method
        self.modelName = modelName
        self.payload = payload
        self.sequence = sequence


class EventFactory(object):
    def __init__(self, validator):
        self.validator = validator

    def create(self, sequence, payload, method):
        self.validator.validate(sequence, payload, method)
        return Event(sequence, payload, method)


class EventLog(object):
    def publish(self, event):
        # route events to logs by event type
        # ensure crud is legit (state machine is able to C/U/D)
        # Write to db
        pass
