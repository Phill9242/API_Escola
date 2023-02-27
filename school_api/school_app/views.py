from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import formAluno, formProfessor, formCurso
from .models import Aluno, Curso, Professor


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
				cleaned_data = form.cleaned_data
				aluno = Aluno(nome=cleaned_data['nome'],
				sobrenome=cleaned_data['sobrenome'],
				dataNascimento=cleaned_data['dataNascimento'],
				dataMatricula=cleaned_data['dataMatricula'])
				aluno.save()
			aluno.cursosMatriculados.set(cleaned_data['cursoMatriculado'])
			aluno.cursosCompletos.set(cleaned_data['cursosCompletos'])
		elif tipo == 'curso':
			form = formCurso(request.POST)
			if form.is_valid():
				curso = Curso(
				nome=form.cleaned_data['nome']
			)
				curso.save()
		elif tipo == 'professor':
			form = formProfessor(request.POST)
		formularioAluno = formAluno()
		formularioCurso = formCurso()
		formularioProfessor = formProfessor()
		return render(request, 'cadastro.html', {'formAluno': formularioAluno, 'formProfessor': formularioProfessor, 'formCurso': formularioCurso})
