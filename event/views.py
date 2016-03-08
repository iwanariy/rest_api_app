# coding: utf-8
# from django.shortcuts import render

# import django_filters
from rest_framework import viewsets

from .models import Event
from .serializer import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

from django.shortcuts import render
APP_NAME = "event"


def index(request):
    return render(request, '%s/index.html' % APP_NAME, {})
