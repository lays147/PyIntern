"""views for coordinators module."""
from django.shortcuts import render
from PyIntern.users.models import Coordinator


# Create your views here.
def home(request):
    """Return home page."""
    return render(
        request,
        'coordinators_home.html',
        {'user': 'Lays'},
    )


def list_coordinators(request):
    """Return list of coordinators on the system."""
    coordinators = Coordinator.objects.all()
    return render(
        request,
        'coordinators_list.html',
        {'coordinators': coordinators},
    )
