"""Form for coordinators."""
from django import forms


class CoordinatorsForm(forms.Form):
    """Coordinators Form."""

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
