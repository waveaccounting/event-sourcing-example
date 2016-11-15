from event_source.exceptions import EventlogPreconditionFailure


class ExpenseEventLogService(object):
    def __init__(self, expense_eventlog_backend):
        self.expense_eventlog_backend = expense_eventlog_backend

    def create_expense(self, expense_data):
        latest_sequence = self.get_latest_sequence(expense_data["expense_id"])
        if latest_sequence != expense_data["sequence"]:
            raise EventlogPreconditionFailure
        self.expense_expense_log_backend.save_event_log(expense_data)


class ExpenseAggregateService(object):
    def __init__(self, expense_aggregate_backend):
        self.expense_aggregate_backend = expense_aggregate_backend

    def save_aggregate(self, expense_aggregate):
        self.expense_aggregate_backend.save_aggregate(expense_aggregate)
