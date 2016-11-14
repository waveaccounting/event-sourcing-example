from django.urls import reverse
from django.test import TestCase, Client


class ExpenseAPIView(TestCase):
    def setUp(self):
        self.c = Client()

    def test_post__simple_create(self):
        payload = {
            "previous_event": None,
            "name": "pycon ticket",
            "amount": "150.0000",
            "date": "2016-11-14T12:34:56",
        }

        response = self.c.post(reverse("event_create"), payload)  # TODO json encoding?

        self.assertEqual(200, resonse.status_code)



