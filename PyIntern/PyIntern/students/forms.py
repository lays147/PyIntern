"""Form for coordinators."""
from django import forms
from .models import Student


class StudentsForm(forms.ModelForm):
    """Students Form."""

    class Meta:
        model = Student
        exclude = ['created_at']

    def clean(self):
        """Clean form."""
        cleaned_data = super().clean()
        pw1 = cleaned_data.get('password1')
        pw2 = cleaned_data.get('password2')

        if pw1 != pw2:
            self.add_error('password2', 'Senhas não conferem.')

        cleaned_data.pop('password1')
        cleaned_data.pop('password2')

        cleaned_data['password'] = pw1
        return cleaned_data

    password1 = forms.CharField(
        label='Senha',
        required=True,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label='Confirme sua senha',
        required=True,
        widget=forms.PasswordInput,
    )
