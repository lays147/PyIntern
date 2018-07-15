"""Form for jobs."""
from datetime import datetime
from django import forms
from .models import Jobs


class JobsForm(forms.ModelForm):
    class Meta:
        model = Jobs
        exclude = ['created_at']
        year = datetime.now().year
        widgets = {
            'end_at': forms.SelectDateWidget(years=range(year, year + 2)),
            'answer_date': forms.SelectDateWidget(years=range(year, year + 2)),
        }
