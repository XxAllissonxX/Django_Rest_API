from django.db import models


class Aluno(models.Model):
    matricula = models.IntegerField()
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    avaliacao = models.IntegerField()

    class Meta:
        ordering = ['nome']
