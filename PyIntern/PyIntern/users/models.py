"""Abstract user model."""
from django.db import models


class User(models.Model):
    """User."""

    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-Mail', unique=True)
    phone = models.CharField('Telefone', max_length=20)
    username = models.CharField('Nome de Usuário', max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta class for user."""

        abstract = True
