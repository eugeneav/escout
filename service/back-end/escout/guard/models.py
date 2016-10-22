from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(default=None)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class PasswordRecoverToken(models.Model):
    email = models.CharField(max_length=255)
    token = models.TextField(default=None)
    created = models.DateTimeField(auto_now_add=True)
