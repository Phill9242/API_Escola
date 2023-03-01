from rest_framework import generics
from .models import Aluno, Professor, Curso
from .serializers import AlunoSerializer, CursoSerializer, ProfessorSerializer
from rest_framework.response import  Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from .forms import validar_cpf

class AlunoList(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursoList(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class ProfessorList(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class AlunoDelete(generics.DestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    lookup_url_kwarg = 'id'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Aluno excluído com sucesso!'}, status=status.HTTP_204_NO_CONTENT)

class CursoDelete(generics.DestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    lookup_url_kwarg = 'id'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Curso excluído com sucesso!'}, status=status.HTTP_204_NO_CONTENT)

class ProfessorDelete(generics.DestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    lookup_url_kwarg = 'id'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Professor excluído com sucesso!'}, status=status.HTTP_204_NO_CONTENT)
    
from django.core.exceptions import ValidationError

class AlunoUpdate(generics.RetrieveUpdateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    lookup_url_kwarg = 'id'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            cpf = serializer.validated_data.get('cpf', None)
            if cpf:
                try:
                    validar_cpf(cpf)
                except IntegrityError:
                    return Response({'cpf': 'Já existe um registro com este CPF.'}, status=status.HTTP_400_BAD_REQUEST)
                except ValidationError as error:
                    return Response({'cpf': error.message}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'message': 'Aluno atualizado com sucesso!'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CursoUpdate(generics.RetrieveUpdateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    lookup_url_kwarg = 'id'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Curso atualizado com sucesso!'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfessorUpdate(generics.RetrieveUpdateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    lookup_url_kwarg = 'id'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            cpf = serializer.validated_data.get('cpf', None)
            if cpf:
                try:
                    validar_cpf(cpf)
                except ValidationError as error:
                    return Response({'cpf': error.message}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'message': 'Professor atualizado com sucesso!'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class AlunoCreate(generics.CreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            cpf = serializer.validated_data.get('cpf', None)
            if cpf:
                try:
                    validar_cpf(cpf)
                except IntegrityError:
                    return Response({'cpf': 'Já existe um registro com este CPF.'}, status=status.HTTP_400_BAD_REQUEST)
                except ValidationError as error:
                    return Response({'cpf': error.message}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'message': 'Aluno cadastrado com sucesso!'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CursoCreate(generics.CreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Curso cadastrado com sucesso!'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfessorCreate(generics.CreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            cpf = serializer.validated_data.get('cpf', None)
            if cpf:
                try:
                    validar_cpf(cpf)
                except ValidationError as error:
                    return Response({'cpf': error.message}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'message': 'Professor cadastrado com sucesso!'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
