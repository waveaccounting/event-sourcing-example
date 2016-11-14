from django.urls import reverse
from django.test import TestCase, Client


class ExpenseAPIView(TestCase):
    def setUp(self):
        self.c = Client()

    def post_payload(self, payload):
        return self.c.post(
            reverse("expense-api"),
            data=payload,
            content_type="application/json"
        )

    def put_payload(self, payload):
        # TODO clean up these test helper methods
        return self.c.put(
            reverse("expense-api"),
            data=payload,
            content_type="application/json"
        )

    def test_post__simple_create(self):
        payload = {
            "amount": "150.0000",
            "date": "2016-11-14T12:34:56",
            "name": "pycon ticket",
            "sequence": 1,
        }

        response = self.post_payload(payload)

        self.assertEqual(201, response.status_code)

    def test_post__bad_data(self):
        response = self.post_payload({})
        self.assertEqual(400, response.status_code)

    def test_put__simple(self):
        # TODO set up previous create record.
        self.fail("Need to have existing create record in the event log")

        payload = {
            "amount": "150.0000",
            "date": "2016-11-14T12:34:56",
            "name": "pycon ticket",
            "sequence": 2,
        }
        response = self.put_payload(payload)

        self.assertEqual(201, response.status_code)

    def test_put__bad_data(self):
        response = self.post_payload({})
        self.assertEqual(400, response.status_code)

    def test_put__does_not_have_previous_create(self):
        payload = {
            "amount": "150.0000",
            "date": "2016-11-14T12:34:56",
            "name": "pycon ticket",
            "sequence": 2,
        }

        response = self.put_payload(payload)

        self.assertEqual(400, response.status_code)

