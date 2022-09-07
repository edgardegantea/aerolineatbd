from django.contrib.auth.models import User, Group
from .models import Ciudad, Estado, Direccion, Aerolinea, AreaTrabajo, Avion, Empleado, Aeropuerto, Viaje, Boleto, Ruta, \
    ReservacionViajes, Pasajero, Tarifa, Pago, Asiento, Student
from rest_framework import viewsets
from rest_framework import permissions
from aero.serializers import UserSerializer, GroupSerializer
from .serializers import CiudadSerializer, EstadoSerializer, DireccionSerializer, AerolineaSerializer, \
    AreaTrabajoSerializer, AvionSerializer, EmpleadoSerializer, AeropuertoSerializer, ViajeSerializer, BoletoSerializer, \
    RutaSerializer, ReservacionViajesSerializer, PasajeroSerializer, TarifaSerializer, PagoSerializer, \
    AsientoSerializer, StudentSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer


class EstadoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    # permission_classes = [permissions.IsAuthenticated]


class DireccionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    # permission_classes = [permissions.IsAuthenticated]


class AerolineaViewSet(viewsets.ModelViewSet):
    queryset = Aerolinea.objects.all()
    serializer_class = AerolineaSerializer


class AreaTrabajoViewSet(viewsets.ModelViewSet):
    queryset = AreaTrabajo.objects.all()
    serializer_class = AreaTrabajoSerializer


class AvionViewSet(viewsets.ModelViewSet):
    queryset = Avion.objects.all()
    serializer_class = AvionSerializer


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer


class AeropuertoViewSet(viewsets.ModelViewSet):
    queryset = Aeropuerto.objects.all()
    serializer_class = AeropuertoSerializer


class ViajeViewSet(viewsets.ModelViewSet):
    queryset = Viaje.objects.all()
    serializer_class = ViajeSerializer


class BoletoViewSet(viewsets.ModelViewSet):
    queryset = Boleto.objects.all()
    serializer_class = BoletoSerializer


class RutaViewSet(viewsets.ModelViewSet):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer


class ReservacionViajesViewSet(viewsets.ModelViewSet):
    queryset = ReservacionViajes.objects.all()
    serializer_class = ReservacionViajesSerializer


class PasajeroViewSet(viewsets.ModelViewSet):
    queryset = Pasajero.objects.all()
    serializer_class = PasajeroSerializer


class TarifaViewSet(viewsets.ModelViewSet):
    queryset = Tarifa.objects.all()
    serializer_class = TarifaSerializer


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer


class AsientoViewSet(viewsets.ModelViewSet):
    queryset = Asiento.objects.all()
    serializer_class = AsientoSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
