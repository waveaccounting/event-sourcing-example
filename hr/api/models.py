from django.db import models

class EventLog(models.Model):
    event_data = models.TextField(blank = False)
    sequence = models.IntegerField(blank = False)
    guid = models.AutoField(primary_key = True)
