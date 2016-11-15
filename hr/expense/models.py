from django.db import models


class ExpenseEventLog(models.Model):
    event_data = models.TextField()
    sequence = models.IntegerField()
    entity_id = models.UUIDField(primary_key=False)


class ExpenseAggregate(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200)
    date = models.DateTimeField()
    entity_id = models.UUIDField(primary_key=True, default=None)
