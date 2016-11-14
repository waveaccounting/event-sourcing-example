from django.urls import reverse
from django.test import TestCase, Client


class ExpenseAPIView(TestCase):
    def setUp(self):
        self.c = Client()

    def post_payload(self, payload):
        return self.c.post(
            reverse("expense-api"),
            payload,
            content_type="application/json"
        )

    def test_post__simple_create(self):
        payload = {
            "previous_event": None,
            "name": "pycon ticket",
            "amount": "150.0000",
            "date": "2016-11-14T12:34:56",
        }

        response = self.post_payload(payload)

        self.assertEqual(201, resonse.status_code)

    def test_post__bad_data(self):
        response = self.post_payload({})
        self.assertEqual(400, resonse.status_code)
