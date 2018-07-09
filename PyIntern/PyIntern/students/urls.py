"""urls for coordinators."""
from django.urls import path
from .views import home, list_students

urlpatterns = [
    path('', home, name='students_home'),
    path('list/', list_students, name='students_list'),
]
