"""views for coordinators module."""
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r
from PyIntern.users.models import Coordinator
from .forms import CoordinatorsForm


@login_required
def home(request):
    """Return home page."""
    return render(
        request,
        'coordinators_home.html',
        {'user': request.user.first_name},
    )


@login_required
def list_coordinators(request):
    """Return list of coordinators on the system."""
    coordinators = Coordinator.objects.all()
    return render(
        request,
        'coordinators_list.html',
        {'coordinators': coordinators},
    )


@login_required
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
