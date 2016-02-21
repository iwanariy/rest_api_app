# coding: utf-8
from __future__ import unicode_literals

from django.db import models


class Event(models.Model):
    """
        Event model
    """
    title = models.CharField(max_length=32)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.encode(u"utf-8")
