"""Form for companies."""
from django import forms


class CompanyForm(forms.Form):
    """Company Form."""

    company_name = forms.CharField(
        label='Nome da Empresa',
        max_length=200,
    )
    cnpj = forms.CharField(
        label='CNPJ',
        max_length=14,
    )
    description = forms.CharField(
        label='Descrição',
        widget=forms.Textarea,
    )
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
