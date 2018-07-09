"""Form for coordinators."""
from django import forms
from PyIntern.users.models import Student


class StudentsForm(forms.Form):
    """Students Form."""

    registration = forms.CharField(
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
    phone = forms.CharField(
        label='Telefone',
        required=True,
        min_length=11,
        max_length=11,
    )
    address = forms.CharField(
        label='Endereço',
        required=True,
    )
    cpf = forms.CharField(
        label='CPF',
        min_length=11,
        max_length=11,
        required=True,
    )
    course = forms.ChoiceField(choices=Student.COURSE, )
    mini_bio = forms.CharField(
        label='Mini Bio',
        widget=forms.Textarea,
        max_length=600,
    )
    birth_date = forms.DateField(
        label='Data de Nascimento',
        input_formats=['%Y-%m-%d'],
    )
    resume = forms.FileField(label='Currículo', required=False)
    competences = forms.CharField(label='Competências')
