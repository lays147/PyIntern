"""urls for coordinators."""
from django.urls import path, re_path
from .views import list_jobs, get_job

urlpatterns = [
    path('', list_jobs, name='list_jobs'),
    re_path(r'^(\d+)/$', get_job, name='get_job'),
]
