"""Main_App URL Configuration"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # localhost/ will run views.py index method
    url(r'^$', views.index),
]

