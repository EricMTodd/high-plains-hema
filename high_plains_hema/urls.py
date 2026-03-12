"""Defines the URL patterns for high_plains_hema."""

from django.urls import path

from . import views

app_name = 'high_plains_hema'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]