"""Model for companies."""
from django.core.validators import RegexValidator
from django.db import models
from PyIntern.users.models import User


class Companies(User):
    """Companies Model."""

    company_name = models.CharField('Nome da Empresa', max_length=200)
    cnpj = models.CharField(
        'CNPJ', max_length=14, validators=[RegexValidator(r'^\d{14}$')])
    description = models.CharField('Descrição', max_length=500)
    approved = models.BooleanField('Cadastro aprovado', default=False)

    class Meta:
        """Meta class for companies."""

        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ('name', )

    def __str__(self):
        return self.company_name
