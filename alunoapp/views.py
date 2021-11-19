from django.shortcuts import render
from rest_framework import generics
from alunoapp.models import Aluno
from alunoapp.serializers import AlunoSerializer
from rest_framework.permissions import AllowAny



class AlunoList(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permitions_class = (AllowAny, )
    


class AlunoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno
    serializer_class = AlunoSerializer
    permitions_class = (AllowAny, )
