from event_source.exceptions import InvalidEventType


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

    def update(self, entity_id, sequence, payload):
        self.validator.validate(payload)
        return UpdateEvent(entity_id, sequence, payload)

    def delete(entity_id, sequence):
        return DeleteEvent(entity_id, sequence)


class EventLog(object):
    def __init__(self, event_log_service, aggregate_service):
        self.event_log_service = event_log_service
        self.aggregate_service = aggregate_service

    def publish(self, event):
        if event is CreateEvent:
            saved_event_log = self.event_log_service.save_create(event)
        elif event is UpdateEvent:
            saved_event_log = self.event_log_service.save_update(event)
        elif event is DeleteEvent:
            saved_event_log = self.event_log_service.save_delete(event)
        else:
            raise InvalidEventType
        self.aggregate_service.save_aggregate(saved_event_log)
        return saved_event_log
