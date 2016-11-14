from django.db import models

class ExpenseEventLog(models.Model):
    event_data = models.TextField(blank = False)
    sequence = models.IntegerField(blank = False)
    guid = models.IntegerField()
