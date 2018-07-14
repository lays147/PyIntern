"""urls for coordinators."""
from django.urls import path
from .views import home, list_coordinators, new_register

urlpatterns = [
    path('', home, name='coordinators_home'),
    path('list/', list_coordinators, name='coordinators_list'),
    path('register/', new_register, name='coordinators_new')
]
