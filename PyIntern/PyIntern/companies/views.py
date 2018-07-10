"""views for companies."""
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r
from PyIntern.users.models import Company
from .forms import CompanyForm


@login_required
def home(request):
    """Return home page."""
    return render(
        request,
        'companies_home.html',
        {'user': request.user.first_name},
    )


@login_required
def list_companies(request):
    """Return list of companies on the system."""
    companies = Company.objects.all()
    return render(
        request,
        'companies_list.html',
        {'companies': companies},
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
        'company_form.html',
        {'form': CompanyForm()},
    )


def create(request):
    """Submit new form."""
    form = CompanyForm(request.POST)
    if not form.is_valid():
        return render(
            request,
            'company_form.html',
            {'form': form},
        )
    Company.objects.create(**form.cleaned_data)
    return HttpResponseRedirect(r('list_coordinators'))
