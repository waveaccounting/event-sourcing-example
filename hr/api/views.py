from rest_framework.views import APIView
from rest_framework.response import Response

from api.validators import ExpenseValidator
from event_source.exceptions import InvalidEvent, EventlogPreconditionFailure
from event_source.constants import EventMethod
from event_source.event_log import EventLog, EventFactory


class ExpenseAPIView(APIView):
    def post(self, request):
        return self._crud(request, EventMethod.CREATE)

    def put(self, request):
        return self._crud(request, EventMethod.UPDATE)

    def delete(self, request):
        return self._crud(request, EventMethod.DELETE)

    def get(self, request):
        pass  # TODO

    def _crud(self, request, method):
        sequence = request.data.sequence

        expense_event_factory = EventFactory(ExpenseValidator)

        try:
            event = expense_event_factory(sequence, request.data, method)
        except (KeyError, InvalidEvent):
            return Response('You broke it', status=400)

        try:
            eventLog = EventLog('Expense')  # Make this something more smarter
            eventLog.publish(event)
        except EventlogPreconditionFailure:
            return Response('You broke it', status=400)

        return Response('Good job', status=201)


class MonthlyExpenseReportAPIView(APIView):
    def get(self, request):
        pass
