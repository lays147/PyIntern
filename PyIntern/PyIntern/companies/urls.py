"""urls for coordinators."""
from django.urls import path, re_path
from .views import home, new_register, list_companies, get_company
from .views import get_candidatures

urlpatterns = [
    path('', home, name='companies_home'),
    path('register/', new_register, name='companies_new'),
    path('list/', list_companies, name='companies_list'),
    re_path(r'^(\d+)/$', get_company, name='companies_get'),
    path('enrolls/', get_candidatures, name='companies_candidatures')
]
