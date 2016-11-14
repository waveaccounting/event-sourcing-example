from django.db import models

class ExpenseEventLog(models.Model):
    event_data = models.TextField()
    sequence = models.IntegerField()
    guid = models.IntegerField()

class ExpenseLogAggregate(models.Model):
    amount = models.DecimalField(max_digits = 7, decimal_places = 2)
    description = models.CharField(max_length = 200)
    date = models.DateTimeField()
