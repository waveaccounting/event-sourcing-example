from rest_framework.views import APIView
from rest_framework.response import Response

from api.validators import ExpenseValidator
from event_source.exceptions import (
    InvalidEvent,
    EventlogPreconditionFailure,
)
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
        expense_event_factory = EventFactory(ExpenseValidator())
        try:
            event = expense_event_factory.create(request.data)
            result = self._crud(event)
        except (InvalidEvent, EventlogPreconditionFailure):
            return Response('You broke it', status=400)
        return Response(result, status=201)

    def put(self, request):
        expense_event_factory = EventFactory(ExpenseValidator())
        try:
            sequence = request.data["sequence"]
            expense_id = request.data["expense_id"]
            event = expense_event_factory.update(expense_id, sequence, request.data)
            self._crud(event)
        except (InvalidEvent, EventlogPreconditionFailure, KeyError):
            return Response('You broke it', status=400)
        return Response(status=204)

    def delete(self, request):
        expense_event_factory = EventFactory(ExpenseValidator)

        try:
            sequence = request.data["sequence"]
            expense_id = request.data["expense_id"]
            event = expense_event_factory.delete(expense_id, sequence)
            self._crud(event)
        except (InvalidEvent, EventlogPreconditionFailure, KeyError):
            return Response('You broke it', status=400)
        return Response(status=204)

    def get(self, request):
        pass  # TODO

    def _crud(self, event):
        event_log_service = ExpenseEventLogService(ExpenseEventlogBackend())
        aggregate_service = ExpenseAggregateService(ExpenseAggregateBackend())
        eventLog = EventLog(
            event_log_service=event_log_service,
            aggregate_service=aggregate_service,
        )
        return eventLog.publish(event)


class MonthlyExpenseReportAPIView(APIView):
    def get(self, request):
        pass
