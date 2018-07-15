"""urls for coordinators."""
from django.urls import path, re_path
from .views import home, list_students, new_register, get_student
from .views import list_subscriptions

urlpatterns = [
    path('', home, name='students_home'),
    path('list/', list_students, name='students_list'),
    path('register/', new_register, name='students_new'),
    re_path(r'^(\d+)/$', get_student, name='students_get'),
    re_path(
        r'^list/subscriptions/(?P<new>\w)',
        list_subscriptions,
        name='students_subscriptions'),
    re_path(
        r'^list/subscriptions/$',
        list_subscriptions,
        name='students_subscriptions'),
]
