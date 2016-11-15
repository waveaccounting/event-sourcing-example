import six
import re

from event_source.exceptions import InvalidEvent


class ExpenseValidator(object):
    def validate(self, data):
        if isinstance(data["amount"], six.string_types):
            raise InvalidEvent('Amount is not a string')

        r = re.compile(r'[0-9]+[.][0-9][0-9]')
        if r.match(data["amount"]) is None:
            raise InvalidEvent('Amount is not decimal format')

        if isinstance(data["date"], six.string_types):
            raise InvalidEvent('Date is not a string')
        if isinstance(data["name"], six.string_types):
            raise InvalidEvent('name is not a string')
        if isinstance(data["sequence"], six.integer_types):
            raise InvalidEvent('Sequence is not an int')

        return True
