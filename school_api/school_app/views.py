from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView
from .forms import formAluno, formProfessor, formCurso, EditarAlunoForm, EditarCursoForm, EditarProfessorForm
from .models import Aluno, Curso, Professor
from django.urls import reverse_lazy
from .cadastro import processar_formulario

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
