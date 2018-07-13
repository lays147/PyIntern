from django.contrib import admin
from PyIntern.users.models import Student

# Register your models here.


class StudentModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration', 'allowed')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'registration', 'cpf')


admin.site.register(Student, StudentModelAdmin)
