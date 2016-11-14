from expense.constants import ExpenseEventType
from expense.services import ExpenseService
from expense.backends import ExpenseBackend


def create_expense(expense_data):
    expense_service = ExpenseService(expense_backend=ExpenseBackend())
    expense_data["event_type"] = ExpenseEventType.CREATE_EXPENSE
    expense_service.create_expense(expense_data)
