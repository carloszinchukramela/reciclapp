from django.db import models

# Create your models here.

class Oferente(models.Model):
    nombre= models.CharField(max_length=200)
    mail= models.EmailField()
    telefono = models.IntegerField()
    movilidad = models.BooleanField()
    horario_contacto=models.DateTimeField()
    #publica = models.ForeignKey()
    
class Desecho(models.Model):
    peso_aprox = models.IntegerField()
    #publica = models.ForeignKey('Oferente')
    #localidad = models.ForeignKey()

class TipoDesecho(models.Model):
    metal=models.BooleanField()
    bombilladeluz=models.BooleanField()
    escombros=models.BooleanField()
    carton=models.BooleanField()
    vidrio=models.BooleanField()
    madera=models.BooleanField()
    desechoselectronicos=models.BooleanField()
    baterias=models.BooleanField()
    