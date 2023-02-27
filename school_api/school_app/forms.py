from django import forms
from .models import Curso


class formCurso(forms.Form):
	tipo = forms.CharField(widget=forms.HiddenInput(), initial='curso')
	nome = forms.CharField(max_length=100, required=True)

class formAluno(forms.Form):
	tipo = forms.CharField(widget=forms.HiddenInput(), initial='aluno')
	nome = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'django-form'}), label='Nome')
	sobrenome = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'django-form'}), label='Sobrenome')
	dataNascimento = forms.DateField(required=True, widget=forms.TextInput(attrs={'placeholder': 'DD/MM/AAAA'}),  label='Data de Nascimento')
	UF = forms.CharField(max_length=2, label='Unidade Federativa (UF)')
	cidade = forms.CharField(max_length=100, label='Cidade')
	endereco_logradouro = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ex: Rua, Avenida, Praça'}),  label='Logradouro')
	endereco_numero = forms.CharField(max_length=40, label='Número e complemento')
	dataMatricula = forms.DateField(required=True, widget=forms.TextInput(attrs={'placeholder': 'DD/MM/AAAA'}),  label='Data de Matrícula')
	cursosMatriculado = forms.MultipleChoiceField(choices=[],  label='Cursos Matriculado:', widget=forms.CheckboxSelectMultiple())
	cursosCompletos = forms.MultipleChoiceField(choices=[],  label='Cursos Finalizados:', required=False, widget=forms.CheckboxSelectMultiple())

	def __init__(self, *args, **kwargs):
		super(formAluno, self).__init__(*args, **kwargs)
		cursos_choices = [(c.nome, c.nome) for c in Curso.objects.all()]
		self.fields['cursosMatriculado'].choices = cursos_choices
		self.fields['cursosCompletos'].choices = cursos_choices
	
class formProfessor(forms.Form):
	tipo = forms.CharField(widget=forms.HiddenInput(), initial='professor')
	nome = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'django-form'}), label='Nome')
	sobrenome = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'django-form'}), label='Sobrenome')
	dataNascimento = forms.DateField(required=True, widget=forms.TextInput(attrs={'placeholder': 'DD/MM/AAAA'}),  label='Data de Nascimento')
	UF = forms.CharField(max_length=2, label='Unidade Federativa (UF)')
	cidade = forms.CharField(max_length=100, label='Cidade')
	endereco_logradouro = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ex: Rua, Avenida, Praça'}),  label='Logradouro')
	endereco_numero = forms.CharField(max_length=40,  label='Número e complemento')
	dataContratacao = forms.DateField(required=True, widget=forms.TextInput(attrs={'placeholder': 'DD/MM/AAAA'}),  label='Data de Contratação')
	cursosLecionados = forms.MultipleChoiceField(choices=[],  label='Cursos Lecionados:', widget=forms.CheckboxSelectMultiple())

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		cursos_choices = [(c.nome, c.nome) for c in Curso.objects.all()]
		self.fields['cursosLecionados'].choices = cursos_choices