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
					aluno.cursosMatriculado.set(cleaned_data['cursosMatriculado'])
					aluno.cursosCompletos.set(cleaned_data['cursosCompletos'])
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
					professor.cursosLecionados.set(cleaned_data['cursosLecionados'])
				except:
					pass
		formularioAluno = formAluno()
		formularioCurso = formCurso()
		formularioProfessor = formProfessor()
		return render(request, 'cadastro.html', {'formAluno': formularioAluno, 'formProfessor': formularioProfessor, 'formCurso': formularioCurso})
