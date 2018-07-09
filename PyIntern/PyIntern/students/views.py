from django.shortcuts import render
from PyIntern.users.models import Student


# Create your views here.
def home(request):
    """Return home page."""
    return render(
        request,
        'students_home.html',
        {'user': 'Lays'},
    )


def list_students(request):
    """Return list of students on the system."""
    students = Student.objects.all()
    return render(
        request,
        'students_list.html',
        {'students': students},
    )
