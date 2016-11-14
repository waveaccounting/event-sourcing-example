from event_source.exceptions import InvalidEvent


class ExpenseValidator(object):
    def validate(data):
        if type(data["amount"]) is not str:
            raise InvalidEvent
        if type(data["date"]) is not str:
            raise InvalidEvent
        if type(data["name"]) is not str:
            raise InvalidEvent
        if type(data["sequence"]) is not int:
            raise InvalidEvent

        return True
