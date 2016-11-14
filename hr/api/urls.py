from django.conf.urls import url
from django.contrib import admin

from api.views import ExpenseApiView

urlpatterns = [
    url(r'^expense/', ExpenseApiView.as_view()),
    url(r'^expense-report/', MonthlyExpenseReportApiView.as_view()),
]
