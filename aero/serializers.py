from django.contrib.auth.models import User, Group
from .models import Ciudad, Estado, Direccion, Aerolinea, AreaTrabajo, Avion, Empleado, Aeropuerto, Viaje, Boleto, Ruta, \
    ReservacionViajes, Pasajero, Tarifa, Pago, Asiento, Student
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CiudadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ciudad
        fields = ['nombre', 'cp', 'fechaCreacion', 'fechaActualizacion']


class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = ['nombreEstado', 'fechaCreacion', 'fechaActualizacion']


class DireccionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direccion
        fields = ['calle', 'numeroInterior', 'numeroExterior', 'cp', 'fechaCreacion', 'fechaActualizacion']


class AerolineaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aerolinea
        fields = ['nombre', 'concesion', 'fechaCreacion', 'fechaActualizacion']


class AreaTrabajoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AreaTrabajo
        fields = ['nombreArea', 'claveArea', 'fechaCreacion', 'fechaActualizacion']


class AvionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Avion
        fields = ['capacidad', 'modelo', 'matricula', 'fabricante', 'horasVuelo', 'fechaCreacion', 'fechaActualizacion']


class EmpleadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellidoPaterno', 'apellidoMaterno', 'sexo', 'clavePasaporte', 'fechaCreacion',
                  'fechaActualizacion']


class AeropuertoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aeropuerto
        fields = ['aeropuertoOrigen', 'aeropuertoDestino', 'telefono', 'fechaCreacion', 'fechaActualizacion']


class ViajeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Viaje
        fields = ['codigoViaje', 'fechaLlegada', 'horaLlegada', 'fechaCreacion', 'fechaActualizacion']


class BoletoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boleto
        fields = ['numeroAsiento', 'horaCompra', 'clase', 'fechaSalida', 'horaSalida', 'fechaCreacion',
                  'fechaActualizacion']


class RutaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ruta
        fields = ['status', 'fechaCreacion', 'fechaActualizacion']


class ReservacionViajesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReservacionViajes
        fields = ['fechaReservacion', 'lugaresReservados', 'fechaCreacion', 'fechaActualizacion']


class PasajeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pasajero
        fields = ['nombrePasajero', 'apellidoPaterno', 'ApellidoMaterno', 'telefono', 'clavePasaporte', 'sexo',
                  'fechaCreacion', 'fechaActualizacion']


class TarifaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarifa
        fields = ['costo', 'fechaCreacion', 'fechaActualizacion']


class PagoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pago
        fields = ['tipoPago', 'cantidad', 'nombreTitular', 'referenciaPago', 'fechaCreacion', 'fechaActualizacion']


class AsientoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asiento
        fields = ['numAsiento', 'disponible', 'fechaCreacion', 'fechaActualizacion']


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['stuname', 'email']
