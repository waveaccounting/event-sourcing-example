from event_source.constants import EventLogType
from event_source.exceptions import InvalidEventLogType
from expense.backends import (
    ExpenseEventlogBackend,
    ExpenseAggregateBackend,
)
from expense.services import (
    ExpenseAggregateService,
    ExpenseEventLogService,
)


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
    def __init__(self, event_log_type):
        self.event_log_type = event_log_type

    def publish(self, event):
        # route events to logs by event type
        # ensure crud is legit (state machine is able to C/U/D)
        # Write to db

        if self.event_log_type == EventLogType.EXPENSE:
            event_log_service = ExpenseEventLogService(expense_eventlog_backend=ExpenseEventlogBackend())
            aggregate_service = ExpenseAggregateService(expense_aggregate_backend=ExpenseAggregateBackend())
            saved_event_log = event_log_service.create_expense(event)
            aggregate_service.save_aggregate(event)
            return saved_event_log
        raise InvalidEventLogType
