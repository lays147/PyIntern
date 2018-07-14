"""Students Table."""
from django.core.validators import RegexValidator
from django.db import models
from taggit.managers import TaggableManager
from PyIntern.users.models import User


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
        'Curso', max_length=2, choices=COURSE, default=INFORMATIONSYSTEMS)
    mini_bio = models.CharField('Mini Biografia', max_length=600)
    cpf = models.CharField(
        'CPF', max_length=11, validators=[RegexValidator(r'^\d{11}$')])
    birth_date = models.DateField('Data de Nascimento')
    resume = models.FileField('Curriculo', upload_to='curriculos/', blank=True)
    allowed = models.BooleanField('Autorizado', default=False)
    competences = TaggableManager('Competências')

    class Meta:
        """Meta class for student."""

        verbose_name = 'Estudante'
        verbose_name_plural = 'Estudantes'
        ordering = ('name', )
