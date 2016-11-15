from django.urls import reverse
from django.test import TestCase, Client

from api.validators import ExpenseValidator


class ExpenseValidatorTest(TestCase):
    def setUp(self):
        self.v = ExpenseValidator()

    def test_empty_payload(self):
        self.assertRaises(Exception, self.v.validate, {})

    def test_payload_missing_amount(self):
        self.assertRaises(Exception, self.v.validate, {
            "date": "2016-11-14T12:34:56",
            "name": "pycon ticket",
            "sequence": 1,
        })

    def test_payload_missing_date(self):
        self.assertRaises(Exception, self.v.validate, {
            "amount": "150.0000",
            "name": "pycon ticket",
            "sequence": 1,
        })

    def test_payload_missing_name(self):
        self.assertRaises(Exception, self.v.validate, {
            "amount": "150.0000",
            "date": "2016-11-14T12:34:56",
            "sequence": 1,
        })

    def test_payload_missing_sequence(self):
        self.assertRaises(Exception, self.v.validate, {
            "amount": "150.0000",
            "date": "2016-11-14T12:34:56",
            "name": "pycon ticket",
        })

    def test_payload_bad_amount_format(self):
        self.assertRaises(Exception, self.v.validate, {
            "amount": "this isn't money",
            "date": "2016-11-14T12:34:56",
            "name": "pycon ticket",
            "sequence": 2,
        })

    def test_payload_valid_shape(self):
        valid = self.v.validate({
            "amount": "150.0000",
            "date": "2016-11-14T12:34:56",
            "name": "pycon ticket",
            "sequence": 2,
        })
        self.assertEqual(True, valid)
