"""Model for Coordinators."""
from django.db import models
from PyIntern.users.models import User


class Coordinator(User):
    """Coordinator."""

    register = models.CharField('Matrícula', max_length=11)

    class Meta:
        """Meta class for coordinator."""

        verbose_name = 'Coordenador'
        verbose_name_plural = 'Coordenadores'
        ordering = ('name', )
