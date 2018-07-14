from django.db import models


# Create your models here.
class Jobs(models.Model):
    """Jobs Model."""

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    requirements = models.CharField(max_length=500)
    benefits = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateField()
    answer_date = models.DateField()
    available = models.BooleanField()


class Candidatures(models.Model):
    """Candidatures Model."""

    company = models.ForeignKey('users.Company', on_delete=models.CASCADE)
    student = models.ForeignKey('users.Student', on_delete=models.CASCADE)
    job = models.ForeignKey('Jobs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
