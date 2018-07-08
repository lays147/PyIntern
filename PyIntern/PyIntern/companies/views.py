from django.shortcuts import render
from PyIntern.users.models import Company


# Create your views here.
def home(request):
    """Return home page."""
    return render(
        request,
        'companies_home.html',
        {'user': 'Lays'},
    )
