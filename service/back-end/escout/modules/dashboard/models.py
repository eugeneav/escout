from django.db import models


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Create your models here.
class Application(Base):
    key = models.CharField(max_length=255)
    name = models.CharField(max_length=255)