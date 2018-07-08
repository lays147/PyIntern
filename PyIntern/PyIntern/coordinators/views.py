"""views for coordinators module."""
from django.shortcuts import render


# Create your views here.
def home(request):
    """Return home page."""
    return render(
        request,
        'coordinators_home.html',
        {'user': 'Lays'},
    )
