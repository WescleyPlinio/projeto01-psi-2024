from django.db import models

class Atleta(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    local_nasc = models.TextField(max_length=250)
    posicao = models.CharField(max_length=15)
    foto = models.ImageField()

    def __str__(self):
        return self.nome