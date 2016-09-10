from django.contrib.auth.models import User
from django.db import models

from escout.guard.models import Account


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


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


class Event(Base):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='Application')
    user_session_id = models.IntegerField(default=None)
    user_timezone = models.IntegerField(default=None)  # var hrs = -(new Date().getTimezoneOffset() / 60)
    name = models.CharField(max_length=256, default=None)
    type = models.CharField(max_length=256, default=None)
    priority = models.SmallIntegerField
    start_time = models.IntegerField(default=None)
    stop_time = models.IntegerField(default=None)
    description = models.TextField(default=None)


# TODO Application team feature. Low Priority
'''
    1. Find user by email
    2. Add user to a team
    3. User see applications and their events where he is a team member
'''


class Team(Base):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)
