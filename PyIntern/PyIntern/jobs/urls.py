"""urls for coordinators."""
from django.urls import path, re_path
from .views import list_jobs, get_job, register_into_job, new_register, list_company_jobs

urlpatterns = [
    path('all/', list_jobs, name='jobs_list'),
    path('', list_company_jobs, name='jobs_list_only_company'),
    re_path(r'^(\d+)/$', get_job, name='jobs_get'),
    re_path(r'^register/(?P<pk_job>\d+)', register_into_job, name='jobs_new'),
    path('new/', new_register, name='jobs_new_position')
]
