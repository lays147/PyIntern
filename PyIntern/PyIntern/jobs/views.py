from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.shortcuts import render, get_object_or_404
from .models import Jobs


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
    return render(
        request,
        'view_job.html',
        {
            'job': data,
        },
    )
