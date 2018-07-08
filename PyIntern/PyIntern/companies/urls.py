"""urls for coordinators."""
from django.urls import path
from .views import home, new_register

urlpatterns = [
    path('', home),
    path('register/', new_register, name='new_company')
]
