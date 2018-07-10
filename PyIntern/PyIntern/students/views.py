"""views for students."""
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r
from PyIntern.users.models import Student
from .forms import StudentsForm


@login_required
def home(request):
    """Return home page."""
    return render(
        request,
        'students_home.html',
        {'user': request.user.first_name},
    )


@login_required
def list_students(request):
    """Return list of students on the system."""
    students = Student.objects.all()
    return render(
        request,
        'students_list.html',
        {'students': students},
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
        'student_form.html',
        {'form': StudentsForm()},
    )


def create(request):
    """Submit new form."""
    form = StudentsForm(request.POST)
    if not form.is_valid():
        return render(
            request,
            'student_form.html',
            {'form': form},
        )
    Student.objects.create(**form.cleaned_data)
    return HttpResponseRedirect(r('students_list'))
