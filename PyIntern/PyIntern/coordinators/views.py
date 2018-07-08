"""views for coordinators module."""
from django.shortcuts import render, resolve_url as r
from django.http import HttpResponseRedirect, HttpResponse
from PyIntern.users.models import Coordinator
from .forms import CoordinatorsForm


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


def new_register(request):
    """Handle request to the form."""
    if request.method == 'POST':
        return create(request)
    return empty_form(request)


def empty_form(request):
    """Crete empty form."""
    return render(
        request,
        'coordinators_form.html',
        {'form': CoordinatorsForm()},
    )


def create(request):
    """Submit new form."""
    form = CoordinatorsForm(request.POST)
    if not form.is_valid():
        return render(
            request,
            'coordinators_form.html',
            {'form': form},
        )
    Coordinator.objects.create(**form.cleaned_data)
    return HttpResponseRedirect(r('list_coordinators'))
