from django.db import models
from django.contrib.auth.models import User
from escout.modules.guard.models import Account


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


# Create your models here.

class CommonEventType:
    name = models.CharField(max_length=255)


class Application(Base):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    personal_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField
    modified = models.DateTimeField(auto_now=True)


class EventType:
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Event(Base):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    message = models.TextField
    priority = models.SmallIntegerField


class Team(Base):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    publications = models.ManyToManyField(User)
