from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DeleteView, FormView, UpdateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import formAluno, formProfessor, formCurso, EditarAlunoForm, EditarCursoForm, EditarProfessorForm
from .models import Aluno, Curso, Professor
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import IntegrityError

@csrf_exempt
def listar_alunos(request):
	alunos = Aluno.objects.all()
	return render(request, 'listar_alunos.html', {'alunos': alunos})

class ListarAlunosView(ListView):
	model = Aluno
	template_name = 'listar_alunos.html'
	context_object_name = 'alunos'

class EditarAlunoView(UpdateView):
	model = Aluno
	form_class = EditarAlunoForm
	template_name = 'editar_aluno.html'

	success_url = reverse_lazy('listar_alunos')

class DeletarAlunoView(DeleteView):
	model = Aluno
	success_url = reverse_lazy('listar_alunos')

class ListarCursosView(ListView):
	model = Curso
	template_name = 'listar_cursos.html'
	context_object_name = 'cursos'

class EditarCursoView(UpdateView):
	model = Curso
	form_class = EditarCursoForm
	template_name = 'editar_curso.html'
	success_url = reverse_lazy('listar_cursos')

class DeletarCursoView(DeleteView):
	model = Curso
	success_url = reverse_lazy('listar_cursos')

class ListarProfessorView(ListView):
	model = Professor
	template_name = 'listar_professores.html'
	context_object_name = 'professores'
	
class EditarProfessorView(UpdateView):
	model = Professor
	form_class = EditarProfessorForm
	template_name = 'editar_professor.html'
	success_url = reverse_lazy('listar_professores')

class DeletarProfessorView(DeleteView):
	model = Professor
	success_url = reverse_lazy('listar_professores')
	
def listar_cursos(request):
	cursos = Curso.objects.all()
	return render(request, 'listar_cursos.html', {'cursos': cursos})

@csrf_exempt
def listar_professores(request):
	professores = Professor.objects.all()
	return render(request, 'listar_professores.html', {'professores': professores})

@csrf_exempt
def buscaGeral(request):
	   return render(request, 'busca.html')

@csrf_exempt
def home(request):
	if (request.method == "GET"):
		formularioAluno = formAluno()
		formularioCurso = formCurso()
		formularioProfessor = formProfessor()
		return render(request, 'home.html', {'formAluno': formularioAluno, 'formProfessor': formularioProfessor,'formCurso': formularioCurso})
	if (request.method == "POST"):
		tipo = request.POST.get('tipo')
		if tipo == 'aluno':
			form = formAluno(request.POST)
			if form.is_valid():
				print ("valido")
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
				except:
					pass
			else:
				messages.error(request, 'Não foi possível fazer o cadastro por conta dos seguintes erros: ')
				for x in form.errors:
					messages.error(request, form.errors[x].as_text())
		elif tipo == 'curso':
			form = formCurso(request.POST)
			if form.is_valid():
				try:
					curso = Curso(
						nome=form.cleaned_data['nome'],
						periodo = form.cleaned_data['periodo']
					)
					curso.save()
				except IntegrityError:
					messages.error(request, 'Já existe um registro com este CPF.')
					pass
				except Exception as e:
					messages.error(request, 'Ocorreu um erro desconhecido no servidor. Por favor, verifique os campos e tente novamente.')
					pass
			else:
				messages.error(request, 'Não foi possível fazer o cadastro por conta dos seguintes erros: ')
				for x in form.errors:
					messages.error(request, form.errors[x].as_text())
		elif tipo == 'professor':
			form = formProfessor(request.POST)
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
				except IntegrityError:
					messages.error(request, 'Já existe um registro com este CPF.')
					pass
				except Exception:
					messages.error(request, 'Ocorreu um erro desconhecido no servidor. Por favor, verifique os campos e tente novamente.')
					pass
			else:
				messages.error(request, 'Não foi possível fazer o cadastro por conta dos seguintes erros: ')
				for x in form.errors:
					messages.error(request, form.errors[x].as_text())
		formularioAluno = formAluno()
		formularioCurso = formCurso()
		formularioProfessor = formProfessor()
		return render(request, 'home.html', {'formAluno': formularioAluno, 'formProfessor': formularioProfessor, 'formCurso': formularioCurso})
