"""views for coordinators module."""
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r
from .models import Coordinator
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
    c_form = form.cleaned_data
    user = User.objects.create_user(
        username=c_form.get('username'),
        password=c_form.get('password'),
        email=c_form.get('email'),
        first_name=c_form.get('name').split()[0],
    )
    group = Group.objects.get(name='Coordinators')
    user.groups.add(group)
    c_form.pop('password')
    Coordinator.objects.create(**c_form)
    return HttpResponseRedirect(r('coordinators_list'))
