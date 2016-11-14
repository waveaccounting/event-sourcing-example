from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import status

from api.serializers import ExpenseSerializer


class ExpenseAPIView(APIView):
    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        serialzer = ExpenseSerializer(data=request.data)
        if serializer.is_valid()
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)


class MonthlyReportAPIView(APIView):
    def get(self, request, format=None):
        pass
