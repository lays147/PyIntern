"""Students Table."""
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
    register = models.IntegerField('Matrícula', unique=True)
    course = models.CharField(
        'Curso', max_length=2, choices=COURSE, default=INFORMATIONSYSTEMS)
    mini_bio = models.CharField('Mini Biografia', max_length=600)
    resume = models.FileField('Curriculo', upload_to='curriculos/', blank=True)
    allowed = models.BooleanField('Autorizado', default=False)
    competences = TaggableManager('Competências')

    class Meta:
        """Meta class for student."""

        verbose_name = 'Estudante'
        verbose_name_plural = 'Estudantes'
        ordering = ('name', )
