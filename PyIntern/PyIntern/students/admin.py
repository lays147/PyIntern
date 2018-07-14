"""Admin definition for students model."""
from django.contrib import admin
from .models import Student


class StudentModelAdmin(admin.ModelAdmin):
    """Student model admin."""

    list_display = ('name', 'registration', 'allowed')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'registration', 'cpf')


admin.site.register(Student, StudentModelAdmin)
