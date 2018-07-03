from django.db import models

# Create your models here.
class Bolao(models.Model):

    ID = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idJogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    GolsPais1 = models.IntegerField()
    GolsPais2 =  models.IntegerField()


class Usuario(models.Model):

    ID = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=100)
    Email = models.CharField(max_length=500)


class Jogo(models.Model):

    ID = models.AutoField(primary_key=True)
    Fase = models.CharField(max_length=100)
    idPais1 = models.IntegerField()
    idPais2 = models.IntegerField()
    Golspais1 = models.IntegerField()
    Golspais2 = models.IntegerField()
    Local = models.CharField(max_length=100)
    Horario = models.DateField()
    LinkYoutube = models.CharField(max_length=500)
    Arbitro =  models.CharField(max_length=100)


class Jogador(models.Model):

    ID = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=100)
    IdPais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    NumeroCamisa = models.IntegerField()
    Posicao = models.CharField(max_length=50)
    Idade = models.IntegerField()
    Clube = models.CharField(max_length=50)


class Pais(models.Model):

    ID = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=100)
    Grupo = models.CharField(max_length=100)
