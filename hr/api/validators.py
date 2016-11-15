from event_source.exceptions import InvalidEvent
import re


class ExpenseValidator(object):
    def validate(self, data):
        if self._isUnicodeString(data["amount"]):
            raise InvalidEvent('Amount is not a string')

        r = re.compile(r'[0-9]+[.][0-9][0-9]')
        if r.match(data["amount"]) is None:
            raise InvalidEvent('Amount is not decimal format')

        if self._isUnicodeString(data["date"]):
            raise InvalidEvent('Date is not a string')
        if self._isUnicodeString(data["name"]):
            raise InvalidEvent('name is not a string')
        if self._isUnicodeString(data["sequence"]):
            raise InvalidEvent('Sequence is not an int')

        return True

    def _isUnicodeString(self, string):
        if string is str:
            return True
        if string is unicode:
            return True

        return False
