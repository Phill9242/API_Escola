# Generated by Django 4.1.7 on 2023-02-28 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0003_alter_aluno_cursoscompletos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='cursosCompletos',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='cursosMatriculado',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='cursosLecionados',
        ),
    ]
