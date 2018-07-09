from django.shortcuts import render


# Create your views here.
def home(request):
    """Return home page."""
    return render(
        request,
        'students_home.html',
        {'user': 'Lays'},
    )
