from django.conf.urls import url
from django.contrib import admin

from api.views import ExpenseAPIView, MonthlyExpenseReportAPIView

urlpatterns = [
    url(r'^expense/', ExpenseAPIView.as_view()),
    url(r'^expense-report/', MonthlyExpenseReportAPIView.as_view()),
]
