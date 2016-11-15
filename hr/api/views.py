from rest_framework.views import APIView
from rest_framework.response import Response

from api.validators import ExpenseValidator
from event_source.exceptions import EventlogPreconditionFailure
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
        expense_event_factory = EventFactory(ExpenseValidator)
        event = expense_event_factory.create(request.data)
        return self._crud(request, event)

    def put(self, request):
        sequence = request.data["sequence"]
        expense_id = request.data["expense_id"]
        expense_event_factory = EventFactory(ExpenseValidator)
        event = expense_event_factory.update(expense_id, sequence, request.data)
        return self._crud(request, event)

    def delete(self, request):
        sequence = request.data["sequence"]
        expense_id = request.data["expense_id"]
        expense_event_factory = EventFactory(ExpenseValidator)
        event = expense_event_factory.delete(expense_id, sequence)
        return self._crud(request, event)

    def get(self, request):
        pass  # TODO

    def _crud(self, event):
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
