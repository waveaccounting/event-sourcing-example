from django.urls import reverse
from django.test import TestCase, Client

create_expense_fixture = {
    "amount": "150.0000",
    "date": "2016-11-14T12:34:56",
    "name": "pycon ticket",
    "sequence": 1,
}

update_expense_fixture = {
    "amount": "150.0000",
    "date": "2016-11-14T12:34:56",
    "name": "pycon ticket",
    "sequence": 2,
}

delete_expense_fixture = {
    "amount": "150.0000",
    "date": "2016-11-14T12:34:56",
    "name": "pycon ticket",
    "sequence": 2,
}


class ExpenseAPIViewTestCase(TestCase):
    """This TestCase is integrations tests for the expense api"""
    def setUp(self):
        self.c = Client()

    def _apply_payload_with_method(self, method, payload):
        return getattr(self.c, method)(
            reverse("expense-api"),
            data=payload,
            content_type="application/json"
        )

    def post_payload(self, payload):
        return self._apply_payload_with_method("post", payload)

    def put_payload(self, payload):
        return self._apply_payload_with_method("put", payload)

    def delete_payload(self, payload):
        return self._apply_payload_with_method("delete", payload)

    def test_post__simple_create(self):
        response = self.post_payload(create_expense_fixture)
        self.assertEqual(201, response.status_code)

    def test_post__bad_data(self):
        response = self.post_payload({})
        self.assertEqual(400, response.status_code)

    def test_put__simple_update(self):
        # TODO set up previous create record.
        self.fail("Need to have existing create record in the event log")

        response = self.put_payload(update_expense_fixture)

        self.assertEqual(201, response.status_code)

    def test_put__bad_data(self):
        response = self.put_payload({})
        self.assertEqual(400, response.status_code)

    def test_put__does_not_have_previous_create(self):
        response = self.put_payload(update_expense_fixture)
        self.assertEqual(400, response.status_code)

    def test_delete__simple_delete(self):
        # TODO set up previous create record.
        self.fail("Need to have existing create record in the event log")

        response = self.delete_payload(delete_expense_fixture)

        self.assertEqual(400, response.status_code)

    def test_delete__bad_data(self):
        response = self.delete_payload({})
        self.assertEqual(400, response.status_code)

    def test_delete__does_not_have_previous_create(self):
        response = self.delete_payload(delete_expense_fixture)
        self.assertEqual(400, response.status_code)
