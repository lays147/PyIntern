"""urls for coordinators."""
from django.urls import path, re_path
from .views import list_jobs, get_job, register_into_job

urlpatterns = [
    path('', list_jobs, name='jobs_list'),
    re_path(r'^(\d+)/$', get_job, name='jobs_get'),
    re_path(r'^register/(?P<pk_job>\d+)', register_into_job, name='jobs_new')
]
