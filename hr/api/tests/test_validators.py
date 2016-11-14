from django.urls import reverse
from django.test import TestCase, Client

from api.validators import ExpenseValidator


class ExpenseValidatorTest(TestCase):
    def setUp(self):
        self.v = ExpenseValidator()

    def test_empty_payload(self, payload):
        return self.v.validate({})

    def test_payload_missing_amount(self):
        return self.v.validate({
            "date": "2016-11-14T12:34:56",
            "name": "pycon ticket",
            "sequence": 1,
        })

    def test_payload_missing_date(self):
        return self.v.validate({
            "amount": "150.0000",
            "name": "pycon ticket",
            "sequence": 1,
        })

    def test_payload_missing_name(self):
        return self.v.validate({
            "amount": "150.0000",
            "date": "2016-11-14T12:34:56",
            "sequence": 1,
        })

    def test_payload_missing_sequence(self):
        return self.v.validate({
            "amount": "150.0000",
            "date": "2016-11-14T12:34:56",
            "name": "pycon ticket",
        })
