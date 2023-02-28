from .forms import formAluno, formProfessor, formCurso
from django.contrib import messages
from .models import Aluno, Curso, Professor
from django.db import IntegrityError

def processar_formulario(request):
	form = checar_tipo_formulario(request)
	if form == None:
		messages.info(request, 'Tipo de formulário inválido')
	return

def checar_tipo_formulario(request):
	tipo = request.POST.get('tipo')
	if tipo == 'aluno':
			return(preencher_form_aluno(formAluno(request.POST), request))	
	if tipo == 'curso':
			return(preencher_form_curso(formCurso(request.POST), request))
	if tipo == 'professor':
			return(preencher_form_professor(formProfessor(request.POST), request))
	return None

def preencher_form_aluno(form, request):
	if form.is_valid():
		try:
			cleaned_data = form.cleaned_data
			aluno = Aluno (nome=cleaned_data['nome'],
			UF = cleaned_data['UF'],
			cidade = cleaned_data['cidade'],
			cpf = cleaned_data['cpf'],
			email = cleaned_data['email'],
			telefone = cleaned_data['telefone'],
			endereco_logradouro = cleaned_data['endereco_logradouro'],
			endereco_complemento = cleaned_data['endereco_complemento'],
			sobrenome =cleaned_data['sobrenome'],
			dataNascimento=cleaned_data['dataNascimento'],
			numeroMatricula=cleaned_data['numeroMatricula'],
			dataMatricula=cleaned_data['dataMatricula'])
			aluno.save()
			messages.success(request, 'Cadastro realizado com sucesso!')
		except IntegrityError:
			messages.info(request, 'Já existe um registro com este CPF.')
			pass
			messages.error(request, 'Ocorreu um erro desconhecido no servidor. Por favor, verifique os campos e tente novamente.')
		except Exception:
			pass
	else:
		messages.info(request, 'Não foi possível fazer o cadastro por conta dos seguintes erros: ')
		for x in form.errors:
			messages.info(request, form.errors[x].as_text())
	return (form)

def preencher_form_curso(form, request):
	if form.is_valid():
		try:
			curso = Curso(
			    nome = form.cleaned_data['nome'],
			    periodo = form.cleaned_data['periodo']
			)
			curso.save()
			messages.success(request, 'Cadastro realizado com sucesso!')
		except Exception:
			messages.error(request, 'Ocorreu um erro desconhecido no servidor. Por favor, verifique os campos e tente novamente.')
			pass
	else:
		messages.info(request, 'Não foi possível fazer o cadastro por conta dos seguintes erros: ')
		for x in form.errors:
			messages.info(request, form.errors[x].as_text())
	return (form)
		
def preencher_form_professor(form, request):		
	if form.is_valid():
		try:
			cleaned_data = form.cleaned_data
			professor = Professor (nome=cleaned_data['nome'],
			sobrenome =cleaned_data['sobrenome'],
			UF = cleaned_data['UF'],
			cidade = cleaned_data['cidade'],
			cpf = cleaned_data['cpf'],
			email = cleaned_data['email'],
			telefone = cleaned_data['telefone'],
			endereco_logradouro = cleaned_data['endereco_logradouro'],
			endereco_complemento = cleaned_data['endereco_complemento'],			
			dataNascimento=cleaned_data['dataNascimento'],
			dataContratacao=cleaned_data['dataContratacao'])
			professor.save()
			messages.success(request, 'Cadastro realizado com sucesso!')
		except IntegrityError:
			messages.info(request, 'Já existe um registro com este CPF.')
			pass
		except Exception:
			messages.error(request, 'Ocorreu um erro desconhecido no servidor. Por favor, verifique os campos e tente novamente.')
			pass
	else:
		messages.info(request, 'Não foi possível fazer o cadastro por conta dos seguintes erros: ')
		for x in form.errors:
			messages.info(request, form.errors[x].as_text())
	return (form)