import json
from uuid import uuid4


class ExpenseEventLogService(object):
    def __init__(self, expense_eventlog_backend):
        self.expense_eventlog_backend = expense_eventlog_backend

    def save_create(self, event):
        event_log_data_to_save = {
            "sequence": 1,
            "event_data": json.dumps(event.payload),
            "entity_id": uuid4(),
        }
        self.expense_eventlog_backend.save_event_log(event_log_data_to_save)

    def save_update(self, event):
        pass

    def save_delete(self, event):
        pass


class ExpenseAggregateService(object):
    def __init__(self, expense_aggregate_backend):
        self.expense_aggregate_backend = expense_aggregate_backend

    def save_aggregate(self, expense_aggregate):
        self.expense_aggregate_backend.save_aggregate(expense_aggregate)
