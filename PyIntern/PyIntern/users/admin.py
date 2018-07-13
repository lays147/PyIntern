from django.contrib import admin

from .models import Student, Coordinator, Company

admin.site.register(Coordinator)
admin.site.register(Company)
