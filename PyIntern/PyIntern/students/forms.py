"""Form for coordinators."""
from django import forms
from .models import Student


class StudentsForm(forms.Form):
    """Students Form."""

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

    register = forms.CharField(
        label='Matrícula',
        required=True,
    )
    name = forms.CharField(
        label='Nome',
        required=True,
    )
    email = forms.EmailField(
        label='E-Mail',
        required=True,
    )
    username = forms.CharField(
        label='Nome de Usuário',
        required=True,
    )
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
    phone = forms.CharField(
        label='Telefone',
        required=True,
        min_length=11,
        max_length=11,
    )
    course = forms.ChoiceField(choices=Student.COURSE, )
    mini_bio = forms.CharField(
        label='Mini Bio',
        widget=forms.Textarea,
        max_length=600,
    )
    resume = forms.FileField(label='Currículo', required=False)
    competences = forms.CharField(label='Competências')
