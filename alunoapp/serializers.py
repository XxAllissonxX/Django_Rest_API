from rest_framework import serializers
from alunoapp.models import Aluno


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id','matricula', 'nome', 'cpf', 'avaliacao']