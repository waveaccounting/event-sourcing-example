from django.urls import reverse
from django.test import TestCase, Client

create_expense_fixture = {
    "amount": "150.0000",
    "date": "2016-11-14T12:34:56",
    "name": "pycon ticket",
    "sequence": 1,
}

update_expense_fixture = {
    "amount": "200.0000",
    "date": "2016-11-14T12:40:00",
    "name": "pycon canada ticket",
    "sequence": 2,
}

delete_expense_fixture = {
    "amount": "150.0000",
    "date": "2016-11-14T12:40:00",
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

    def get_expense(self, query_string={}):
        return self.c.get(
            reverse("expense-api"),
            query_string,
            content_type="application/json"
        )

    def post_payload(self, payload):
        return self._apply_payload_with_method("post", payload)

    def put_payload(self, payload):
        return self._apply_payload_with_method("put", payload)

    def delete_payload(self, payload):
        return self._apply_payload_with_method("delete", payload)

    def _create_inital_expense_event_in_log(self):
        # TODO I am not sure I love creating this with the api. It could cause
        # other tests to fail.
        response = self.post_payload(create_expense_fixture)
        self.assertEqual(201, response.status_code)

    def _update_expense_event_in_log(self):
        # TODO I am not sure I love creating this with the api. It could cause
        # other tests to fail.
        response = self.put_payload(update_expense_fixture)
        self.assertEqual(201, response.status_code)

    def _mark_expense_as_deleted_event_in_log(self):
        # TODO I am not sure I love creating this with the api. It could cause
        # other tests to fail.
        response = self.delete_payload(delete_expense_fixture)
        self.assertEqual(201, response.status_code)

    def test_post__simple_create(self):
        response = self.post_payload(create_expense_fixture)
        self.assertEqual(201, response.status_code)

    def test_post__bad_data(self):
        response = self.post_payload({})
        self.assertEqual(400, response.status_code)

    def test_put__simple_update(self):
        self._create_inital_expense_event_in_log()

        response = self.put_payload(update_expense_fixture)

        self.assertEqual(201, response.status_code)

    def test_put__bad_data(self):
        response = self.put_payload({})
        self.assertEqual(400, response.status_code)

    def test_put__does_not_have_previous_create(self):
        response = self.put_payload(update_expense_fixture)
        self.assertEqual(400, response.status_code)

    def test_delete__simple_delete(self):
        self._create_inital_expense_event_in_log()

        response = self.delete_payload(delete_expense_fixture)

        self.assertEqual(400, response.status_code)

    def test_delete__bad_data(self):
        response = self.delete_payload({})
        self.assertEqual(400, response.status_code)

    def test_delete__does_not_have_previous_create(self):
        response = self.delete_payload(delete_expense_fixture)
        self.assertEqual(400, response.status_code)

    def test_get__simple(self):
        expected = {
            "amount": "150.0000",
            "date": "2016-11-14T12:34:56",
            "name": "pycon ticket",
            "sequence": 1,
        }  # ??? Anything else?

        self._create_inital_expense_event_in_log()

        response = self.get_expense()

        self.assertEqual(200, response.status_code)
        self.assertDictEqual(expected, response.data)

    def test_get__at_time__before_existance(self):
        self._create_inital_expense_event_in_log()
        self._update_expense_event_in_log()

        # Try to get the state of the expense the month before it existed
        response = self.get_expense({"datetime": "2016-10-14T12:34:56"})

        # ??? Should this have a different status code?
        self.assertEqual(404, response.status_code)

    def test_get__at_time__before_update(self):
        expected = {
            "amount": "150.0000",
            "date": "2016-11-14T12:34:56",
            "name": "pycon ticket",
            "sequence": 1,
        }  # ??? Anything else?

        self._create_inital_expense_event_in_log()
        self._update_expense_event_in_log()

        # Get the state of the expense before it was updated
        response = self.get_expense({"datetime": "2016-11-14T12:35:00"})

        self.assertEqual(200, response.status_code)
        self.assertDictEqual(expected, response.data)

    def test_get__at_time__after_update(self):
        expected = {
            "amount": "200.0000",
            "date": "2016-11-14T12:40:00",
            "name": "pycon canada ticket",
            "sequence": 2,
        }  # ??? Anything else?

        self._create_inital_expense_event_in_log()
        self._update_expense_event_in_log()

        # Get the state of the expense before it was updated
        response = self.get_expense({"datetime": "2016-12-14T12:50:00"})

        self.assertEqual(200, response.status_code)
        self.assertDictEqual(expected, response.data)

    def test_get__at_time__before_delete(self):
        expected = {
            "amount": "150.0000",
            "date": "2016-11-14T12:34:56",
            "name": "pycon ticket",
            "sequence": 1,
        }  # ??? Anything else?

        self._create_inital_expense_event_in_log()
        self._mark_expense_as_deleted_event_in_log()

        # Get the state of the expense before it was updated
        response = self.get_expense({"datetime": "2016-11-14T12:35:00"})

        self.assertEqual(200, response.status_code)
        self.assertDictEqual(expected, response.data)

    def test_get__at_time__after_delete(self):
        self._create_inital_expense_event_in_log()
        self._mark_expense_as_deleted_event_in_log()

        # Get the state of the expense before it was updated
        response = self.get_expense({"datetime": "2016-12-14T12:50:00"})

        # ??? Should this a different status code?
        self.assertEqual(400, response.status_code)
