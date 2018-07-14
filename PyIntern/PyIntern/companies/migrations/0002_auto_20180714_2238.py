# Generated by Django 2.0.4 on 2018-07-14 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-Mail'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='username',
            field=models.CharField(max_length=20, unique=True, verbose_name='Nome de Usuário'),
        ),
    ]
