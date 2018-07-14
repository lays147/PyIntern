"""views for students."""
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r, get_object_or_404
from .models import Student
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
    c_form = form.cleaned_data
    user = User.objects.create_user(
        username=c_form.get('username'),
        password=c_form.get('password1'),
        email=c_form.get('email'),
        first_name=c_form.get('name').split()[0],
    )
    group = Group.objects.get(name='Students')
    user.groups.add(group)
    c_form.pop('password1')
    c_form.pop('password2')

    Student.objects.create(**c_form)
    return HttpResponseRedirect(r('students_list'))


@login_required
def get_student(request, register):
    """Student file."""
    student = get_object_or_404(Student, registration=register)
    data = model_to_dict(student)
    return render(
        request,
        'students_record.html',
        {
            'student': data,
        },
    )
