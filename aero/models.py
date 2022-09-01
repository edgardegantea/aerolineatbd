from django.db import models
# Create your models here.

class Aerolinea(models.Model):
    nombre = models.CharField(verbose_name='Nombre de la Aerolinea', max_length=60)
    concesion = models.CharField(verbose_name='Concesion', max_length=30)


    def __str__(self):
        return self.nombre

class AreaTrabajo(models.Model):
    nombreArea = models.CharField(verbose_name='Area de Trabajo', max_length=50)
    claveArea = models.CharField(verbose_name='Clave de area', max_length=10)

    def __str__(self):
        return self.nombreArea

class Avion(models.Model):
    capacidad = models.IntegerField(verbose_name='Capacidad del Avion', max_length=10)
    modelo = models.CharField(verbose_name='Modelo del Avion', max_length=10)
    matricula = models.CharField(verbose_name='Matricula', max_length=10)
    fabricante = models.CharField(verbose_name='Fabricante', max_length=25)
    horasVuelo = models.