"""urls for coordinators."""
from django.urls import path
from .views import home

urlpatterns = [
    path('', home),
]
