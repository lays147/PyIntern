"""urls for coordinators."""
from django.urls import path
from .views import home, list_students, new_register

urlpatterns = [
    path('', home, name='students_home'),
    path('list/', list_students, name='list_students'),
    path('register/', new_register, name='new_student'),
]
