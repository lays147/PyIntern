# Generated by Django 2.0.4 on 2018-07-14 20:59

import django.core.validators
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('registration', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.CharField(choices=[('SI', 'Sistemas de Informação'), ('CC', 'Ciêncida da Computação'), ('SC', ' Tecnólogo em Sistemas de Computação')], default='SI', max_length=2, verbose_name='Curso')),
                ('mini_bio', models.CharField(max_length=600, verbose_name='Mini Biografia')),
                ('cpf', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^\\d{11}$')], verbose_name='CPF')),
                ('birth_date', models.DateField(verbose_name='Data de Nascimento')),
                ('resume', models.FileField(blank=True, upload_to='curriculos/', verbose_name='Curriculo')),
                ('allowed', models.BooleanField(default=False, verbose_name='Autorizado')),
                ('competences', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Competências')),
            ],
            options={
                'verbose_name': 'Estudante',
                'verbose_name_plural': 'Estudantes',
                'ordering': ('name',),
            },
        ),
    ]