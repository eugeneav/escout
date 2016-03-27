from django.db import models


# Basic Event entity which is responsible for tracking client events
class Event(models.Model):
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=256)
    description = models.TextField
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
