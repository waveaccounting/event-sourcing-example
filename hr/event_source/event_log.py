from event_source.constants import EventLogType
from expense.backends import (
    ExpenseEventlogBackend,
    ExpenseAggregateBackend,
)
from expense.services import (
    ExpenseAggregateService,
    ExpenseEventLogService,
)


class Event(object):
    def __init__(self, sequence, method, payload, modelName):
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
            return event
        raise Exception("invalid event log type")
