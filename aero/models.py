from django.db import models

SEXO = (('Femenino', 'Femenino'), ('Masculino', 'Masculino'))
DISPONIBILIDAD = (('Libre', 'Libre'), ('Ocupado', 'Ocupado'))


class Aerolinea(models.Model):
    nombre = models.CharField(verbose_name='Nombre de la Aerolinea', max_length=60)
    concesion = models.CharField(verbose_name='Concesion', max_length=30)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class AreaTrabajo(models.Model):
    nombreArea = models.CharField(verbose_name='Area de Trabajo', max_length=50)
    claveArea = models.CharField(verbose_name='Clave de area', max_length=10)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombreArea


class Avion(models.Model):
    capacidad = models.IntegerField(verbose_name='Capacidad del Avion')
    modelo = models.CharField(verbose_name='Modelo del Avion', max_length=10)
    matricula = models.CharField(verbose_name='Matricula', max_length=10)
    fabricante = models.CharField(verbose_name='Fabricante', max_length=25)
    horasVuelo = models.TimeField(verbose_name='Horas de Vuelo')
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.modelo


class Empleado(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=60)
    apellidoPaterno = models.CharField(verbose_name='Apellido Paterno', max_length=40)
    apellidoMaterno = models.CharField(verbose_name='Apellido Materno', max_length=40)
    sexo = models.CharField(choices=SEXO, default='Femenino', max_length=9,
                            verbose_name='Seleccione el sexo del Empleado')
    clavePasaporte = models.CharField(verbose_name='Ingrese la clave del pasaporte', max_length=20)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} {1}".format(self.nombre, self.apellidoPaterno)


class Aeropuerto(models.Model):
    aeropuertoOrigen = models.CharField(verbose_name='Nombre del aeropueerto de origen', max_length=30)
    aeropuertoDestino = models.CharField(verbose_name='Nombre del aeropueerto de destino', max_length=30)
    telefono = models.CharField(verbose_name='Ingrese el numero de Telefono', max_length=20)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.aeropuertoOrigen


class Viaje(models.Model):
    codigoViaje = models.CharField(verbose_name='Ingrese el codigo de su viaje', max_length=50)
    fechaLlegada = models.DateField(verbose_name='Fecha de Llegada del viaje')
    horaLlegada = models.TimeField(verbose_name='Hora de Legada del viaje')
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.codigoViaje


class Boleto(models.Model):
    numeroAsiento = models.CharField(verbose_name='Ingrese el numero de Asiento asignado', max_length=10)
    horaCompra = models.TimeField(auto_now_add=True)
    clase = models.CharField(verbose_name='Ingrese el tipo de clase del boleto', max_length=10)
    fechaSalida = models.DateField(verbose_name='Ingrese la fecha de salida del Viaje')
    horaSalida = models.TimeField(verbose_name='Ingrese la hora de salida del viaje')
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.numeroAsiento


class Ciudad(models.Model):
    nombre = models.CharField(verbose_name='Nombre de la ciudad', max_length=80)
    cp = models.IntegerField(verbose_name='codigo postal')
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Estado(models.Model):
    nombreEstado = models.CharField(verbose_name='Nombre del estado', max_length=80)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombreEstado


class Direccion(models.Model):
    calle = models.CharField(verbose_name='Nonbre dela calle', max_length=50)
    numeroInterior = models.CharField(verbose_name='numero interior', max_length=4)
    numeroExterior = models.CharField(verbose_name='numero exterior', max_length=4)
    cp = models.CharField(verbose_name='Codigo postal', max_length=10)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.calle


class Ruta(models.Model):
    status = models.CharField(verbose_name='status de la ruta', max_length=80)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status


class ReservacionViajes(models.Model):
    fechaReservacion = models.DateTimeField(auto_now_add=True)
    lugaresReservados = models.CharField(verbose_name='Numero de lugar', max_length=4)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fechaReservacion


class Pasajero(models.Model):
    nombrePasajero = models.CharField(verbose_name='Nombre del pasajero', max_length=80)
    apellidoPaterno = models.CharField(verbose_name='Apellido paterno', max_length=50)
    apellidoMaterno = models.CharField(verbose_name='Apellido materno', max_length=50)
    telefono = models.CharField(verbose_name='Telefono del pasajero', max_length=13)
    clavePasaporte = models.CharField(verbose_name='Clave de pasaporte', max_length=20)
    sexo = models.CharField(verbose_name='Sexo del pasajero', max_length=15)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombrePasajero


class Tarifa(models.Model):
    costo = models.DecimalField(verbose_name='Costo tarifa', max_digits=5, decimal_places=2)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.costo


class Pago(models.Model):
    tipoPago = models.CharField(verbose_name='tipo de pago', max_length=30)
    cantidad = models.DecimalField(verbose_name='Cantidad a pagar', max_digits=5, decimal_places=2)
    nombreTitular = models.CharField(verbose_name='Nombre del titular', max_length=80)
    referenciaPago = models.CharField(verbose_name='Referencia de pago', max_length=30)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombreTitular


class Asiento(models.Model):
    numAsiento = models.SmallIntegerField(verbose_name='Numero de aseinto')
    disponible = models.CharField(choices=DISPONIBILIDAD, default='Libre', max_length=7, verbose_name='Seleccione la '
                                                                                                      'disponibilidad'
                                                                                                      ' del asiento')
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.numAsiento


class Student(models.Model):
    stuname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
