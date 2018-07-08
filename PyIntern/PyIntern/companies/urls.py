"""urls for coordinators."""
from django.urls import path
from .views import home, new_register, list_companies

urlpatterns = [
    path('', home),
    path('register/', new_register, name='new_company'),
    path('list/', list_companies, name='list_companies')
]
