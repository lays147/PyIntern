"""Form for companies."""
from django import forms
from .models import Companies


class CompanyForm(forms.ModelForm):
    """Company Form."""

    class Meta:
        model = Companies
        exclude = ['created_at', 'approved']

    def clean(self):
        """Clean form."""
        cleaned_data = super().clean()
        pw1 = cleaned_data.pop('password1', 0)
        pw2 = cleaned_data.pop('password2', 1)
        if pw1 != pw2:
            self.add_error('password2', 'Senhas não conferem.')
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
