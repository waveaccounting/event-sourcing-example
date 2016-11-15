from event_source.exceptions import InvalidEvent
import re


class ExpenseValidator(object):
    def validate(self, data):
        if type(data["amount"]) is not str:
            raise InvalidEvent('Amount is not a string')

        r = re.compile(r'[0-9]+[.][0-9][0-9]')
        if r.match(data["amount"]) is None:
            raise InvalidEvent('Amount is not decimal format')

        if type(data["date"]) is not str:
            raise InvalidEvent('Date is not a string')
        if type(data["name"]) is not str:
            raise InvalidEvent('name is not a string')
        if type(data["sequence"]) is not int:
            raise InvalidEvent('Sequence is not an int')

        return True
