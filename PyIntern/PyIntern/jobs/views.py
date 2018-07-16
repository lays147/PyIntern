from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r, get_object_or_404
from PyIntern.companies.models import Companies
from PyIntern.students.models import Student
from .models import Jobs, Candidatures
from .forms import JobsForm


# Create your views here.
@login_required
def list_jobs(request):
    """Return list of jobs on the system."""
    jobs = Jobs.objects.all().filter(available=True)
    return render(
        request,
        'jobs_list.html',
        {'jobs': jobs},
    )


@login_required
def list_company_jobs(request):
    """Return list of jobs on the system."""
    company = get_object_or_404(Companies, username=request.user.username)
    jobs = Jobs.objects.all().filter(company=company).filter(available=True)
    return render(
        request,
        'jobs_list.html',
        {'jobs': jobs},
    )


@login_required
def get_job(request, id):
    """Jobs file."""
    job = get_object_or_404(Jobs, id=id)
    data = model_to_dict(job)
    data['company'] = model_to_dict(job.company)
    is_student = request.user.groups.filter(name='Students').exists()
    return render(
        request,
        'view_job.html',
        {
            'job': data,
            'student': is_student,
        },
    )


@login_required
def register_into_job(request, pk_job):
    """Register into job."""
    student = get_object_or_404(Student, username=request.user.username)
    job = get_object_or_404(Jobs, id=pk_job)
    company = get_object_or_404(Companies, id=job.company.id)
    already_subscribed = Candidatures.objects.all().filter(
        student=student).filter(job=job)
    if not student.allowed:
        return HttpResponseRedirect(r('students_home', allowed=False))
    if already_subscribed:
        return HttpResponseRedirect(r('students_subscriptions'))
    Candidatures.objects.create(
        student=student,
        company=company,
        job=job,
    )
    return HttpResponseRedirect(r('students_subscriptions', new=True))


def new_register(request):
    """Handle request to the form."""
    if request.method == 'POST':
        return create(request)
    return empty_form(request)


def empty_form(request):
    """Crete empty form."""
    company = get_object_or_404(Companies, username=request.user.username)
    return render(
        request,
        'jobs_form.html',
        {'form': JobsForm(initial={'company': company})},
    )


@login_required
def create(request):
    company = get_object_or_404(Companies, username=request.user.username)
    form = JobsForm(request.POST, initial={'company': company})
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(r('jobs_list_only_company'))
    return render(request, 'jobs_form.html', {'form': form})
