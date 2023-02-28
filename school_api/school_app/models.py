from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class Curso(models.Model):
	nome = models.CharField(max_length=100, unique=True)
	periodo = models.CharField(choices=[
        ('matutino', 'Matutino'),
        ('vespertino', 'Vespertino'),
        ('noturno', 'Noturno')
    ], max_length=20)

class Professor(models.Model):
	nome = models.CharField(max_length=30)
	sobrenome = models.CharField(max_length=50)
	cpf = models.CharField(unique=True, max_length=14)
	UF = models.CharField(max_length=2)
	email = models.EmailField(max_length=140)
	telefone = models.CharField(max_length=14)
	cidade = models.CharField(max_length=100)
	endereco_logradouro = models.CharField(max_length=100)
	endereco_complemento = models.CharField(max_length=40)
	dataNascimento = models.DateField()
	dataContratacao = models.DateField()
	regimeContratacao = models.CharField(choices=[
        ('temporario', 'Temporário'),
        ('clt', 'CLT'),
        ('pj', 'PJ')
    ], max_length=20)
	
class Aluno(models.Model):
	nome = models.CharField(max_length=30)
	sobrenome = models.CharField(max_length=50)
	cpf = models.CharField(unique=True, max_length=14)
	email = models.EmailField(max_length=140)
	telefone = models.CharField(max_length=14)
	UF = models.CharField(max_length=2)
	cidade = models.CharField(max_length=100)
	endereco_logradouro = models.CharField(max_length=100)
	endereco_complemento = models.CharField(max_length=40)
	dataNascimento = models.DateField()
	dataMatricula = models.DateField()
	numeroMatricula = models.CharField(max_length=10)

