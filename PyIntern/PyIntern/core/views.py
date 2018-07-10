"""views for core."""
from django.shortcuts import render, resolve_url as r
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    """Return home page."""
    if request.method == "POST":
        return log_user(request)
    return render(request, 'index.html')


def log_user(request):
    """Auth the user."""
    user = request.POST.get('user')
    password = request.POST.get('pwd')
    auth = authenticate(request, username=user, password=password)
    if auth is None:
        return render(request, 'index.html', {'error': True})
    else:
        login(request, auth)
        if auth.groups.filter(name='Coordinators').exists():
            return HttpResponseRedirect(r('coordinators_home'))
        elif auth.groups.filter(name='Companies').exists():
            return HttpResponseRedirect(r('companies_home'))
        elif auth.groups.filter(name='Students').exists():
            return HttpResponseRedirect(r('students_home'))


def log_user_out(request):
    """Logout the user."""
    logout(request)
    return HttpResponseRedirect(r('home'))
