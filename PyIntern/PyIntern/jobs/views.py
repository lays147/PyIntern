from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Jobs


# Create your views here.
@login_required
def list_jobs(request):
    """Return list of jobs on the system."""
    jobs = Jobs.objects.all()
    return render(
        request,
        'jobs_list.html',
        {'jobs': jobs},
    )
