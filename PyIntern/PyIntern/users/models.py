from django.core.validators import RegexValidator
from django.db import models


class User(models.Model):
    """User."""

    registration = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    username = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        """Return user name."""
        return self.name


class Company(User):
    """Company."""

    company_name = models.CharField(max_length=200)
    cnpj = models.CharField(
        max_length=14, validators=[RegexValidator(r'^\d{14}$')])
    description = models.CharField(max_length=500)
