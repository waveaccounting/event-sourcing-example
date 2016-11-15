class ExpenseEventlogBackend(object):
    def save_event_log(self, expense_data_validator):
        '''
        Use Django ORM to persist data
        '''
        pass

    def get_latest_sequence(self, expense_id):
        pass


class ExpenseAggregateBackend(object):
    def save_aggregate(self, expense_aggregate):
        pass
