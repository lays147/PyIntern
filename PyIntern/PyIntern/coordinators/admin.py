"""Admin definition for coordinators model."""
from django.contrib import admin
from .models import Coordinator


class CoordinatorModelAdmin(admin.ModelAdmin):
    """Coordinator model admin."""

    list_display = ('name', 'register')
    date_hierarchy = 'created_at'
    search_fields = ('name', )


admin.site.register(Coordinator, CoordinatorModelAdmin)
