from django.db import models




class Ciudad (models.Model):
    nombre = models.CharField(verbose_name='Nombre de la ciudad', max_length=80)
    cp = models.IntegerField(verbose_name= 'codigo postal', max_length=10)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
