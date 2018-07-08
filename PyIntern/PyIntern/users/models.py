from django.db import models
from django.core.validators import RegexValidator
from taggit.managers import TaggableManager


class User(models.Model):
    """User."""

    registration = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    username = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        """Return user name."""
        return self.name


class Student(User):
    """Student."""

    INFORMATIONSYSTEMS = 'SI'
    COMPUTERSCIENCE = 'CC'
    COMPUTERINFORMATION = 'SC'
    COURSE = (
        (INFORMATIONSYSTEMS, 'Sistemas de Informação'),
        (COMPUTERSCIENCE, 'Ciêncida da Computação'),
        (COMPUTERINFORMATION, ' Tecnólogo em Sistemas de Computação'),
    )

    course = models.CharField(
        max_length=2, choices=COURSE, default=INFORMATIONSYSTEMS)
    mini_bio = models.CharField(max_length=600)
    cpf = models.CharField(
        max_length=11, validators=[RegexValidator(r'^\d{11}$')])
    birth_date = models.DateField()
    resume = models.FileField(upload_to='curriculos/', blank=True)
    allowed = models.BooleanField(default=False)
    competences = TaggableManager()


class Coordinator(User):
    """Coordinator."""

    cpf = models.CharField(max_length=11)


class Company(User):
    """Company."""

    company_name = models.CharField(max_length=200)
    cnpj = models.CharField(
        max_length=14, validators=[RegexValidator(r'^\d{14}$')])
    description = models.CharField(max_length=500)
