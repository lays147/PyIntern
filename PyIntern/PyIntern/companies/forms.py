"""Form for companies."""
from django import forms


class CompanyForm(forms.Form):
    """Company Form."""

    def clean(self):
        """Clean form."""
        cleaned_data = super().clean()
        pw1 = cleaned_data.get('password1')
        pw2 = cleaned_data.get('password2')
        if pw1 != pw2:
            self.add_error('password2', 'Senhas não conferem.')
        return cleaned_data

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
    address = forms.CharField(
        label='Endereço',
        required=True,
    )
