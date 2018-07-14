"""Admin definition for companies model."""
from django.contrib import admin
from .models import Companies


class CompaniesModelAdmin(admin.ModelAdmin):
    """Companies model admin."""

    list_display = ('company_name', 'name', 'email')
    date_hierarchy = 'created_at'
    search_fields = ('company_name', )


admin.site.register(Companies, CompaniesModelAdmin)
