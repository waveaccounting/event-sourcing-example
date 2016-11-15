class Event(object):
    pass


class CreateEvent(Event):
    def __init__(self, payload):
        self.payload = payload
        self.sequence = 0


class UpdateEvent(Event):
    def __init__(self, entity_id, sequence, payload):
        self.entity_id = entity_id
        self.payload = payload
        self.sequence = sequence


class DeleteEvent(Event):
    def __init__(self, entity_id, sequence):
        self.entity_id = entity_id
        self.sequence = sequence


class EventFactory(object):
    def __init__(self, validator):
        self.validator = validator

    def create(self, payload):
        self.validator.validate(payload)
        return CreateEvent(payload)

    def update(self, event_id, sequence, payload):
        self.validator.validate(payload)
        return UpdateEvent(entity_id, sequence, payload)

    def delete(entity_id, sequence):
        return DeleteEvent(entity_id, sequence)


class EventLog(object):
    def __init__(self, event_log_service, aggregate_service):
        self.event_log_service = event_log_service
        self.aggregate_service = aggregate_service

    def publish(self, event):
        saved_event_log = self.event_log_service.create_expense(event)
        self.aggregate_service.save_aggregate(event)
        return saved_event_log
