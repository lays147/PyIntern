"""views for companies."""
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
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
            'student_form.html',
            {'form': form},
        )
    c_form = form.cleaned_data
    user = User.objects.create_user(
        username=c_form.get('username'),
        password=c_form.get('password1'),
        email=c_form.get('email'),
        first_name=c_form.get('name').split()[0],
    )
    group = Group.objects.get(name='Companies')
    user.groups.add(group)
    c_form.pop('password1')
    c_form.pop('password2')

    Company.objects.create(**c_form)
    return HttpResponseRedirect(r('company_home'))
