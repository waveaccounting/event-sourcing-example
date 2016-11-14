from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import status

from api.validators import ExpenseValidator
from event_source.exceptions import InvalidEvent, EventlogPreconditionFailure
from event_source.constants import EventMethod
from event_source.event_log import EventLog, EventFactory


class ExpenseAPIView(APIView):
    def post(self, request):
        self._crud(self, request, EventMethod.CREATE)

    def put(self, request):
        self._crud(self, request, EventMethod.UPDATE)

    def delete(self, request):
        self._crud(self, request, EventMethod.DELETE)

    def get(self, request):
        pass  # TODO

    def _crud(self, request, method):
        sequence=request.data.sequence

        expense_event_factory = EventFactory(ExpenseValidator)

        try:
            event = expense_event_factory(sequence, request.data, method)
        except InvalidEvent:
            return Response('You broke it', status=status.HTTP_400_BAD_REQUEST)

        try:
            EventLog.publish(event)
        except EventlogPreconditionFailure:
            return Response('You broke it', status=status.HTTP_400_BAD_REQUEST)

        return Response('Good job', status=status.HTTP_201_CREATED)


class MonthlyReportAPIView(APIView):
    def get(self, request, format=None):
        pass
