"""urls for coordinators."""
from django.urls import path, re_path
from .views import home, list_students, new_register, get_student

urlpatterns = [
    path('', home, name='students_home'),
    path('list/', list_students, name='list_students'),
    path('register/', new_register, name='new_student'),
    re_path(r'^(\d+)/$', get_student, name='get_student'),
]
