# coding: utf-8
from __future__ import unicode_literals

from django.db import models


class Event(models.Model):
    """
        Event model
    """
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name.encode(u"utf-8")
