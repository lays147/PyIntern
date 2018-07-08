"""urls for coordinators."""
from django.urls import path
from .views import home, list_coordinators, new_register

urlpatterns = [
    path('', home),
    path('list/', list_coordinators, name='list_coordinators'),
    path('register/', new_register, name='new_coordinator')
]
