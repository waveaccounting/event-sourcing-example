from django.db import models


class ExpenseEventLog(models.Model):
    event_data = models.TextField()
    sequence = models.IntegerField()
    guid = models.IntegerField()
