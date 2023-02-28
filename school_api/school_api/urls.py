"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school_app.views import *

urlpatterns = [
	path('', home, name='home'),
	path('admin/', admin.site.urls),
	path('alunos/', ListarAlunosView.as_view(), name='listar_alunos'),
	path('cursos/', ListarCursosView.as_view(), name='listar_cursos'),
	path('professores/', ListarProfessorView.as_view(), name='listar_professores'),
    path('deletar_aluno/<int:pk>/', DeletarAlunoView.as_view(), name='deletar_aluno'),
    path('deletar_curso/<int:pk>/', DeletarCursoView.as_view(), name='deletar_curso'),
    path('deletar_professor/<int:pk>/', DeletarProfessorView.as_view(), name='deletar_professor'),
    path('editar_aluno/<int:pk>/', EditarAlunoView.as_view(), name='editar_aluno'),
    path('editar_curso/<int:pk>/', EditarCursoView.as_view(), name='editar_curso'),
    path('editar_professor/<int:pk>/', EditarProfessorView.as_view(), name='editar_professor')
]
