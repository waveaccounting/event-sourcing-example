from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import status

from api.serializers import EventMethod, InvalidEvent, EventlogPreconditionFailure, EventLog, EventFactory, ExpenseValidator

class ExpenseAPIView(APIView):
    def dispatch(self, request):
        if request.method == request.GET:
            pass # TODO

        sequence=request.data.sequence

        expenseEventFactory = EventFactory(ExpenseValidator)

        try:
            event = expenseEventFactory(
                sequence,
                request.data,
                self._getMethod(request.method)
            )
        except InvalidEvent:
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            eventlog.publish(event)
        except EventlogPreconditionFailure:
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serialzer.data, status=status.HTTP_201_CREATED)

    def _getMethod():
        if request.method == request.POST:
            return EventMethod.CREATE
        if request.method == request.PUT:
            return EventMethod.UPDATE
        if request.method == request.DELETE:
            return EventMethod.DELETE


class MonthlyReportAPIView(APIView):
    def get(self, request, format=None):
        pass
