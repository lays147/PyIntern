from django.shortcuts import render, resolve_url as r
from django.http import HttpResponseRedirect
from PyIntern.users.models import Company
from .forms import CompanyForm


# Create your views here.
def home(request):
    """Return home page."""
    return render(
        request,
        'companies_home.html',
        {'user': 'Lays'},
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
