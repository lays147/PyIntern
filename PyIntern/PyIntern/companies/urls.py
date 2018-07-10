"""urls for coordinators."""
from django.urls import path, re_path
from .views import home, new_register, list_companies, get_company

urlpatterns = [
    path('', home, name='company_home'),
    path('register/', new_register, name='new_company'),
    path('list/', list_companies, name='list_companies'),
    re_path(r'^(\d+)/$', get_company, name='get_company'),
]
