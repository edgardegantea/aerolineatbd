from django.db import models




class Ciudad (models.Model):
    nombre = models.CharField(verbose_name='Nombre de la ciudad', max_length=80)
    cp = models.IntegerField(verbose_name='codigo postal', max_length=10)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
class Estado (models.Model):
    nombreEstado= models.CharField(verbose_name='Nombre del estado', max_length=80)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombreEstado

class Direccion (models.Model):
    calle = models.CharField(verbose_name='Nonbre dela calle', max_length=50)
    numeroInterior = models.CharField(verbose_name='numero interior', max_length=4)
    numeroExterior = models.CharField(verbose_name='numero exterior', max_length=4)
    cp = models.CharField(verbose_name='Codigo postal', max_length=10)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.calle


class Ruta (models.Model):
    status = models.CharField(verbose_name='status de la ruta', max_length=80)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.status
    
class reservacionViajes (models.Model):
    fechaReservacion = models.DateTimeField(auto_now_add=True)
    lugaresReservados = models.CharField(verbose_name='Numero de lugar', max_length=4)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fechaReservacion

class Pasajero (models.Model):
    nombrePasajero = models.CharField(verbose_name='Nombre del pasajero', max_length=80)
    apellidoPaterno = models.CharField(verbos_name='Apellido paterno', max_length=50)
    apellidoMaterno = models.CharField(verbose_name='Apellido materno', max_length=50)
    telefono = models.CharField(verbose_name='Telefono del pasajero', max_length=13)
    clavePasaporte = models.CharField(verbose_name='Clave de pasaporte', max_length=20)
    sexo = models.CharField(verbose_name='Sexo del pasajero', max_length=15)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombrePasajero

class tarifa (models.Model):
    costo = models.DecimalField(verbose_name='Costo tarifa', max_digits=10)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.costo

class Pago (models.Model)
    tipoPago = models.CharField(verbose_name='tipo de pago', max_length=30)
    cantidad = models.DecimalField(verbose_name='Cantidad a pagar', max_digits=10)
    nombreTitular = models.CharField(verbose_name='Nombre del titular', max_length=80)
    referenciaPago = models.CharField(verbose_name='Referencia de pago', max_length=30)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombreTitular

class Asiento (models.Model):
    numAsiento = models.SmallIntegerField(verbose_name='Numero de aseinto', max_length=3)
    disponible = models.CharField(verbose_name='Disnponibilidad del asiento', max_length=20)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.numAsiento