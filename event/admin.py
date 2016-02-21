# encoding: utf-8
from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
        Admin class for Event
    """
    list_display = (u"title", u"description", u"created_at", u"updated_at")
