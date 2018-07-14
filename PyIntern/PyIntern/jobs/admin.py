from django.contrib import admin
from .models import Candidatures, Jobs


class JobsModelAdmin(admin.ModelAdmin):
    """Jobs model admin."""

    list_display = ('name', 'created_at', 'end_at')
    date_hierarchy = 'created_at'
    search_fields = ('name', )


class CandidaturesModelAdmin(admin.ModelAdmin):
    """Candidatures model admin."""

    list_display = ('get_student_name', 'get_job_name', 'created_at')
    date_hierarchy = 'created_at'

    # search_fields = ('job.name', )

    def get_student_name(self, obj):
        """return students name."""
        return obj.student.name

    get_student_name.short_description = 'Aluno(a)'

    def get_job_name(self, obj):
        """return job name."""
        return obj.job.name

    get_job_name.short_description = 'Vaga'


admin.site.register(Candidatures, CandidaturesModelAdmin)
admin.site.register(Jobs, JobsModelAdmin)
