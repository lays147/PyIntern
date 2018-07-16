"""views for companies."""
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r, get_object_or_404
from .models import Companies
from .forms import CompanyForm
from PyIntern.jobs.models import Candidatures


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
    companies = Companies.objects.all()
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
        password=c_form.pop('password'),
        email=c_form.get('email'),
        first_name=c_form.get('name').split()[0],
    )
    group = Group.objects.get(name='Companies')
    user.groups.add(group)
    Companies.objects.create(**c_form)

    return HttpResponseRedirect(r('home'))


@login_required
def get_company(request, register):
    """company file."""
    company = get_object_or_404(Companies, registration=register)
    data = model_to_dict(company)
    return render(
        request,
        'company_record.html',
        {
            'company': data,
        },
    )


@login_required
def get_candidatures(request):
    """return list of students candidatures."""
    company = get_object_or_404(Companies, username=request.user.username)
    candidatures = Candidatures.objects.all().filter(company=company)
    return render(
        request,
        'companies_list_enroll.html',
        {'candidatures': candidatures},
    )
