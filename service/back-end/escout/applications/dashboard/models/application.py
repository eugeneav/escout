from . import Base
from django.db import models


class Application(Base):
    key = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
