from expense.models import ExpenseEventLog


class ExpenseEventlogBackend(object):
    def save_event_log(self, expense_event_data):
        saved_event_log = ExpenseEventLog.objects.create(**expense_event_data)
        return saved_event_log

    def get_latest_sequence(self, expense_id):
        return 0


class ExpenseAggregateBackend(object):
    def save_aggregate(self, expense_aggregate):
        pass
