# coding: utf-8

from django.conf.urls import url
from rest_framework import routers
from .views import EventViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'event', EventViewSet)


urlpatterns = [
    url(u"^$", views.index),
]
