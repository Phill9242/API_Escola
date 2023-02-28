from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class Curso(models.Model):
	nome = models.CharField(max_length=100, unique=True)

class Professor(models.Model):
	nome = models.CharField(max_length=30)
	sobrenome = models.CharField(max_length=50)
	cidade = models.CharField(max_length=100)
	UF = models.CharField(max_length=2)
	endereco_logradouro = models.CharField(max_length=100)
	endereco_numero = models.CharField(max_length=40)
	dataContratacao = models.DateField()

	
class Aluno(models.Model):
	nome = models.CharField(max_length=30)
	sobrenome = models.CharField(max_length=50)
	cidade = models.CharField(max_length=100)
	UF = models.CharField(max_length=2)
	endereco_logradouro = models.CharField(max_length=100)
	endereco_numero = models.CharField(max_length=40)
	dataNascimento = models.DateField()
	dataMatricula = models.DateField()

