from event_source.exceptions import InvalidEvent
import re


class ExpenseValidator(object):
    def validate(self, data):
        r = re.compile(r'[0-9]+[.][0-9][0-9]')
        if r.match(data["amount"]) is None:
            raise InvalidEvent('Amount is not decimal format')

        return True
