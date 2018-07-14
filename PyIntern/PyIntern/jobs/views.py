from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r, get_object_or_404
from .models import Jobs, Candidatures
from PyIntern.users.models import Company
from PyIntern.students.models import Student


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
    company = get_object_or_404(Company, registration=job.company.registration)
    Candidatures.objects.create(
        student=student,
        company=company,
        job=job,
    )
    return HttpResponseRedirect(r('students_home'))
