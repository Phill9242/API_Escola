from django import forms
from .models import Curso, Aluno


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

class EditarAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'dataNascimento' : 'Data de Nascimento',
            'UF' : 'Unidade Federativa (UF)',
            'cidade' : 'Cidade',
            'endereco_logradouro': 'Logradouro',
	        'endereco_numero': 'Número e Complemento',
		    'dataMatricula': 'Data de Matrícula'
        }