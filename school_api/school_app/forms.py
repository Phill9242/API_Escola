from django import forms
from .models import MyModel, Curso

class MyForm(forms.ModelForm):
	class Meta:
		model = MyModel
		fields = ('title', 'description', 'completed')
	def __str__(self):
		return self.title


class formCurso(forms.Form):
	tipo = forms.CharField(widget=forms.HiddenInput(), initial='curso')
	nome = forms.CharField(max_length=100, required=True)

class formAluno(forms.Form):
	tipo = forms.CharField(widget=forms.HiddenInput(), initial='aluno')
	nome = forms.CharField(max_length=30)
	sobrenome = forms.CharField(max_length=50)
	dataNascimento = forms.DateField(required=True)
	dataMatricula = forms.DateField(required=True)
	cursoMatriculado = forms.MultipleChoiceField(choices=[])
	cursosCompletos = forms.MultipleChoiceField(choices=[])

	def __init__(self, *args, **kwargs):
		super(formAluno, self).__init__(*args, **kwargs)
		cursos = Curso.objects.all().values_list('id', 'nome')
		self.fields['cursoMatriculado'].choices = cursos
		self.fields['cursosCompletos'].choices = cursos
	
class formProfessor(forms.Form):
	tipo = forms.CharField(widget=forms.HiddenInput(), initial='professor')
	nome = forms.CharField(max_length=30)
	sobrenome = forms.CharField(max_length=50)		
