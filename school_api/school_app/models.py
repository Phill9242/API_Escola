from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class MyModel(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	completed = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class Curso(models.Model):
	nome = models.CharField(max_length=100)

class Professor(models.Model):
	nome = models.CharField(max_length=30)
	sobrenome = models.CharField(max_length=50)
	
class Aluno(models.Model):
	nome = models.CharField(max_length=30)
	sobrenome = models.CharField(max_length=50)
	dataNascimento = models.DateField()
	dataMatricula = models.DateField()
	cursosMatriculados = models.ManyToManyField(Curso)
	cursosCompletos = models.ManyToManyField(Curso, related_name='completos')
