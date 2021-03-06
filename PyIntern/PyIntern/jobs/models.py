from django.db import models


class Jobs(models.Model):
    """Jobs Model."""

    company = models.ForeignKey(
        'companies.Companies',
        verbose_name='Empresa',
        on_delete=models.CASCADE)
    name = models.CharField('Nome da Vaga', max_length=100)
    description = models.CharField('Descrição', max_length=500)
    requirements = models.CharField('Requisitos', max_length=500)
    benefits = models.CharField('Benefícios', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateField('Data de Encerramento')
    answer_date = models.DateField('Data de Retorno')
    available = models.BooleanField('Inscrições Disponíveis')

    class Meta:
        """Meta class for Jobs."""

        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
        ordering = ('name', )

    def __str__(self):
        return self.name


class Candidatures(models.Model):
    """Candidatures Model."""

    company = models.ForeignKey(
        'companies.Companies',
        verbose_name='Empresa',
        on_delete=models.CASCADE)
    student = models.ForeignKey(
        'students.Student', verbose_name='Estudante', on_delete=models.CASCADE)
    job = models.ForeignKey(
        'Jobs', verbose_name='Vaga', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta class for Candidatures."""

        verbose_name = 'Candidatura'
        verbose_name_plural = 'Candidaturas'
        ordering = ('created_at', )
