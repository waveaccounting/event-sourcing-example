import date
from decimal import Decimal


class ExpenseBackend(object):
    def save_event_log(self, expenese_data):
        '''
        Use Django ORM to persist data
        '''
        expense_data = {
            "event_data": {
                "amount": Decimal("10.00"),
                "name": "Lunch",
                "date": date.datetime.now(),
            },
            "sequence": 1,
            "expense_id": 1,
            "event_type": "CREATE",
        }

    def get_latest_sequence(self, expense_id):
        pass
