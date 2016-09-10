from django.contrib.auth.models import User
from django.db import models

from escout.guard.models import Account


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
    description = models.TextField(default=None)
    modified = models.DateTimeField(auto_now=True)

    @classmethod
    def create(cls, account, personal_id, title, description):
        application = cls()
        application.account = account
        application.personal_id = personal_id
        application.title = title
        application.description = description
        application.save()
        return cls


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
