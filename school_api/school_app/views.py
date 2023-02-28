from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DeleteView, FormView, UpdateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import formAluno, formProfessor, formCurso, EditarAlunoForm
from .models import Aluno, Curso, Professor
from django.urls import reverse_lazy

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

class ListarProfessorView(ListView):
    model = Professor
    template_name = 'listar_professores.html'
    context_object_name = 'professores'
    
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
def cadastroHTML(request):
	if (request.method == "GET"):
		formularioAluno = formAluno()
		formularioCurso = formCurso()
		formularioProfessor = formProfessor()
		return render(request, 'cadastro.html', {'formAluno': formularioAluno, 'formProfessor': formularioProfessor,'formCurso': formularioCurso})
	if (request.method == "POST"):
		tipo = request.POST.get('tipo')
		if tipo == 'aluno':
			form = formAluno(request.POST)
			if form.is_valid():
				try:
					cleaned_data = form.cleaned_data
					aluno = Aluno (nome=cleaned_data['nome'],
					UF = cleaned_data['UF'],
					cidade=cleaned_data['cidade'],
					endereco_logradouro = cleaned_data['endereco_logradouro'],
					endereco_numero = cleaned_data['endereco_numero'],
					sobrenome=cleaned_data['sobrenome'],
					dataNascimento=cleaned_data['dataNascimento'],
					dataMatricula=cleaned_data['dataMatricula'])
					aluno.save()
				except:
					pass
		elif tipo == 'curso':
			form = formCurso(request.POST)
			if form.is_valid():
				try:
					curso = Curso(
					nome=form.cleaned_data['nome']
					)
					curso.save()
				except:
					pass
		elif tipo == 'professor':
			form = formProfessor(request.POST)
			if form.is_valid():
				try:
					cleaned_data = form.cleaned_data
					professor = Professor (nome=cleaned_data['nome'],
					sobrenome=cleaned_data['sobrenome'],
					UF = cleaned_data['UF'],
					cidade=cleaned_data['cidade'],
					endereco_logradouro = cleaned_data['endereco_logradouro'],
					endereco_numero = cleaned_data['endereco_numero'],
					dataContratacao=cleaned_data['dataContratacao'])
					professor.save()
				except:
					pass
		formularioAluno = formAluno()
		formularioCurso = formCurso()
		formularioProfessor = formProfessor()
		return render(request, 'cadastro.html', {'formAluno': formularioAluno, 'formProfessor': formularioProfessor, 'formCurso': formularioCurso})
