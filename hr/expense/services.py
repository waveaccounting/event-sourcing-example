
class ExpenseService(object):
    def __init__(self, expense_backend):
        self.expense_backend = expense_backend

    def create_expense(self, expense_data):
        latest_sequence = self.get_latest_sequence(expense_data["expense_id"])
        if latest_sequence + 1 != expense_data["sequence"]:
            raise Exception
        self.expense_backend.save_event_log(expense_data)
