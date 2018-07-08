"""urls for coordinators."""
from django.urls import path
from .views import home, list_coordinators

urlpatterns = [
    path('', home),
    path('list', list_coordinators, name='list_coordinators'),
]
