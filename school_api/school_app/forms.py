from django import forms
from .models import Curso, Aluno, Professor
from django.core.exceptions import ValidationError
import re

def validar_cpf(value):
    if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', value):
        raise ValidationError('CPF inválido.')

class formCurso(forms.Form):
    tipo = forms.CharField(widget=forms.HiddenInput(), initial='curso')
    nome = forms.CharField(max_length=100, required=True)
    periodo = forms.ChoiceField(choices=[
        ('matutino', 'Matutino'),
        ('vespertino', 'Vespertino'),
        ('noturno', 'Noturno')
    ], widget=forms.RadioSelect, label='Período')

class formAluno(forms.Form):
    tipo = forms.CharField(widget=forms.HiddenInput(), initial='aluno')
    nome = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'django-form'}), label='Nome')
    sobrenome = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'django-form'}), label='Sobrenome')
    dataNascimento = forms.DateField(required=True, widget=forms.TextInput(attrs={'placeholder': 'DD/MM/AAAA'}),  label='Data de Nascimento',     error_messages={
        'invalid': 'Por favor, insira uma data de nascimento válida no formato DD/MM/AAAA.'
    })
    cpf = forms.CharField(validators=[validar_cpf], required=True, widget=forms.TextInput(attrs={'placeholder': '000.000.000-00'}),  label='CPF', error_messages={
        'duplicate': 'CPF Já Cadastrado!'
    })
    email = forms.EmailField(label='E-Mail')
    telefone = forms.CharField(max_length=14, required=True, widget=forms.TextInput(attrs={'placeholder': '(00)0000-0000'}),  label='Telefone')
    UF = forms.CharField(max_length=2, label='Unidade Federativa (UF)')
    cidade = forms.CharField(max_length=100, label='Cidade')
    endereco_logradouro = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ex: Rua, Avenida, Praça'}),  label='Logradouro')
    endereco_complemento = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Ex: Nº 13, Bloco 4, apartamento 20'}), label='Número e complemento')
    dataMatricula = forms.DateField(required=True, widget=forms.TextInput(attrs={'placeholder': 'DD/MM/AAAA'}),  label='Data de Matrícula', error_messages={
        'invalid': 'Por favor, insira uma data de matrícula válida no formato DD/MM/AAAA.'
    })
    numeroMatricula = forms.CharField(max_length=10, label='Número de Matrícula',  widget=forms.TextInput(attrs={'placeholder': '00000000.0'}))

class formProfessor(forms.Form):
    tipo = forms.CharField(widget=forms.HiddenInput(), initial='professor')
    nome = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'django-form'}), label='Nome')
    sobrenome = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'django-form'}), label='Sobrenome')
    dataNascimento = forms.DateField(required=True, widget=forms.TextInput(attrs={'placeholder': 'DD/MM/AAAA'}),  label='Data de Nascimento', error_messages={
        'invalid': 'Por favor, insira uma data de nascimento válida no formato DD/MM/AAAA.'
    })
    cpf = forms.CharField(validators=[validar_cpf], required=True, widget=forms.TextInput(attrs={'placeholder': '000.000.000-00'}),  label='CPF', error_messages={
        'duplicate': 'CPF Já Cadastrado!'
    })
    email = forms.EmailField(label='E-Mail')
    telefone = forms.CharField(max_length=14, required=True, widget=forms.TextInput(attrs={'placeholder': '(00)0000-0000'}),  label='Telefone')
    UF = forms.CharField(max_length=2, label='Unidade Federativa (UF)')
    cidade = forms.CharField(max_length=100, label='Cidade')
    endereco_logradouro = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ex: Rua, Avenida, Praça'}),  label='Logradouro')
    endereco_complemento = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Ex: Nº 13, Bloco 4, apartamento 20'}), label='Número e complemento')
    dataContratacao = forms.DateField(required=True, widget=forms.TextInput(attrs={'placeholder': 'DD/MM/AAAA'}),  label='Data de Contratação', error_messages={
        'invalid': 'Por favor, insira uma data de contratação válida no formato DD/MM/AAAA.'
    })
    regimeContratacao = forms.ChoiceField(choices=(
        ('temporario', 'Temporário'),
        ('clt', 'CLT'),
        ('pj', 'PJ'),
    ), widget=forms.RadioSelect, label='Regime de Contratação')


class EditarAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'dataNascimento' : 'Data de Nascimento',
            'cpf': 'CPF',
            'email' : 'E-Mail',
            'telefone' : 'Telefone',
            'UF' : 'Unidade Federativa (UF)',
            'cidade' : 'Cidade',
            'endereco_logradouro': 'Logradouro',
            'endereco_complemento': 'Número e Complemento',
            'dataMatricula': 'Data de Matrícula',
            'numeroMatricula' : 'Número de Matrícula'
        }

class EditarProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'dataNascimento' : 'Data de Nascimento',
            'cpf': 'CPF',
            'email' : 'E-Mail',
            'telefone' : 'Telefone',
            'UF' : 'Unidade Federativa (UF)',
            'cidade' : 'Cidade',
            'endereco_logradouro': 'Logradouro',
            'endereco_complemento': 'Número e Complemento',
            'dataContratacao': 'Data de Contratação',
            'regimeContratacao' : 'Regime de Contratação'
        }

class EditarCursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'periodo' : 'Periodo'
        }