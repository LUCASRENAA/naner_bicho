from django.contrib.auth.models import User
from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

#Dinheiro
class Dinheiro(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    def get_valor(self):
        return self.valor
    def get_usuario(self):
        return self.usuario


#Jogar
class Evento(models.Model):

    milhar = models.DecimalField(max_digits=4, decimal_places=0)
    rodada = models.IntegerField()
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    conferir = models.DecimalField(max_digits = 19,decimal_places = 2)
    conferir2 = models.DecimalField ( max_digits = 19, decimal_places = 2 )
    conferir3 = models.DecimalField ( max_digits = 19, decimal_places = 2 )
    conferir4 = models.DecimalField ( max_digits = 19, decimal_places = 2 )
    conferir5 = models.DecimalField ( max_digits = 19, decimal_places = 2 )
    pule = models.IntegerField()

#1 ganhou 0 perdeu
    def get_conferir(self):
        return self.conferir
    def get_pule(self):
        return self.pule
    def get_conferir2(self):
        return self.conferir2
    def get_conferir3(self):
        return self.conferir3
    def get_conferir4(self):
        return self.conferir4
    def get_conferir5(self):
        return self.conferir5
    class Meta:
        db_table = 'evento'

    def get_milhar(self):
        return self.milhar
    def get_rodada(self):
        return self.rodada
    def get_usuario(self):
        return self.usuario
    def get_valor(self):
        return self.valor

#Rodada
class Rodada(models.Model):
    rodada = models.IntegerField()
    primeira_milhar = models.IntegerField()
    segunda_milhar = models.IntegerField()
    terceira_milhar = models.IntegerField()
    quarta_milhar = models.IntegerField()
    quinta_milhar = models.IntegerField()
    data_criacao = models.DateTimeField ( auto_now = True )
    data = models.CharField(max_length=18)

    def get_data(self):
        return self.data


    def get_rodada(self):
        return self.rodada
    def get_primeira_milhar(self):
        return self.primeira_milhar
    def get_segunda_milhar(self):
        return self.segunda_milhar
    def get_terceira_milhar(self):
        return self.terceira_milhar
    def get_quarta_milhar(self):
        return self.quarta_milhar
    def get_quinta_milhar(self):
        return self.quinta_milhar

#padronizando as apostas
class Aposta(models.Model):
    usuario =models.ForeignKey(User,on_delete=models.CASCADE)
    aposta = models.DecimalField(max_digits=19, decimal_places=2)


    def get_aposta(self):
        return self.aposta

    def get_usuario(self):
        return self.usuario

class avaliacao(models.Model):
    usuario =models.ForeignKey(User,on_delete = models.CASCADE)
    avaliacao = models.IntegerField()
    def get_usuario(self):
        return self.usuario
    def get_avaliacao(self):
        return self.avaliacao


class Avaliacao_teste(models.Model):
    usuario =models.ForeignKey(User,on_delete = models.CASCADE)
    avaliacao = models.IntegerField()
    descricao = models.TextField()
    def get_usuario(self):
        return self.usuario
    def get_avaliacao(self):
        return self.avaliacao
    def get_descricao(self):
        return self.descricao



class Online_esta(models.Model):
    usuario = models.ForeignKey(User,models.CASCADE)
    data = models.CharField(max_length = 18)
    def get_data(self):
        return self.data







class Localizacao(models.Model):
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    usuario = models.ForeignKey(User,on_delete = models.CASCADE)
    def get_latitude(self):
        return self.latitude
    def get_longitude(self):
        return self.longitude

    data_evento = models.DateTimeField(auto_now=True)

    class Meta2:
        db_table = 'localizacao'

    def get_data_evento(self):
        return self.data_evento.strftime ( '%d/%m/%Y %H:%M Hrs' )
# Create your models here.
