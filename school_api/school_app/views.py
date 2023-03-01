from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView
from .forms import formAluno, formProfessor, formCurso, EditarAlunoForm, EditarCursoForm, EditarProfessorForm, validar_cpf
from .models import Aluno, Curso, Professor
from django.urls import reverse_lazy
from .cadastro import processar_formulario
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt



class ListarAlunosView(ListView):
	model = Aluno
	template_name = 'listar_alunos.html'
	context_object_name = 'alunos'
	
class EditarAlunoView(UpdateView):
	model = Aluno
	form_class = EditarAlunoForm
	template_name = 'editar_aluno.html'

	success_url = reverse_lazy('listar_alunos')

	def form_valid(self, form):
		aluno = form.save(commit=False)
		cpf = form.cleaned_data['cpf']
		try:
			validar_cpf(cpf)
		except IntegrityError:
			form.add_error('cpf', 'Já existe um registro com este CPF.')
			return self.form_invalid(form)
		except ValidationError as error:
			messages.info(self.request, error.message)
			return self.form_invalid(form)
		
		aluno.save()
		messages.success(self.request, 'Aluno atualizado com sucesso!')
		return super().form_valid(form)
	
	def form_invalid(self, form):
		response = super().form_invalid(form)
		if 'cpf' in form.errors:
			form.errors['cpf'] = None
			messages.info(self.request, 'Já existe um registro com este CPF.')
		return response
	
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
	
	def form_valid(self, form):
		professor = form.save(commit=False)
		cpf = form.cleaned_data['cpf']
		try:
			validar_cpf(cpf)
		except IntegrityError:
			form.add_error('cpf', 'Já existe um registro com este CPF.')
			return self.form_invalid(form)
		except ValidationError as error:
			messages.info(self.request, error.message)
			return self.form_invalid(form)
		
		professor.save()
		messages.success(self.request, 'Professor atualizado com sucesso!')
		return super().form_valid(form)
	
	def form_invalid(self, form):
		response = super().form_invalid(form)
		if 'cpf' in form.errors:
			form.errors['cpf'] = None
			messages.info(self.request, 'Já existe um registro com este CPF.')
		return response
	
class DeletarProfessorView(DeleteView):
	model = Professor
	success_url = reverse_lazy('listar_professores')
	
def home(request):
	if (request.method == "GET"):
		formularioAluno = formAluno()
		formularioCurso = formCurso()
		formularioProfessor = formProfessor()
		return render(request, 'home.html', {'formAluno': formularioAluno, 'formProfessor': formularioProfessor,'formCurso': formularioCurso})
	if (request.method == "POST"):
		processar_formulario(request)
		formularioAluno = formAluno()
		formularioCurso = formCurso()
		formularioProfessor = formProfessor()
		return render(request, 'home.html', {'formAluno': formularioAluno, 'formProfessor': formularioProfessor, 'formCurso': formularioCurso})
