from rest_framework.views import APIView
from rest_framework.response import Response

from api.validators import ExpenseValidator
from event_source.exceptions import InvalidEvent, EventlogPreconditionFailure
from event_source.constants import EventMethod
from event_source.event_log import EventLog, EventFactory
from expense.backends import (
    ExpenseEventlogBackend,
    ExpenseAggregateBackend,
)
from expense.services import (
    ExpenseEventLogService,
    ExpenseAggregateService,
)


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
        expense_event_factory = EventFactory(ExpenseValidator())

        try:
            sequence = request.data["sequence"]
            event = expense_event_factory.create(sequence, request.data, method)
        except (KeyError, InvalidEvent):
            return Response('You broke it', status=400)

        try:
            event_log_service = ExpenseEventLogService(ExpenseEventlogBackend())
            aggregate_service = ExpenseAggregateService(ExpenseAggregateBackend())
            eventLog = EventLog(
                event_log_service=event_log_service,
                aggregate_service=aggregate_service,
            )
            eventLog.publish(event)
        except EventlogPreconditionFailure:
            return Response('You broke it', status=400)

        return Response('Good job', status=201)


class MonthlyExpenseReportAPIView(APIView):
    def get(self, request):
        pass
