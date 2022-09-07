from django.urls import include, path
from rest_framework import routers
from aero import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'ciudad', views.CiudadViewSet)
router.register(r'estado', views.EstadoViewSet)
router.register(r'direccion', views.DireccionViewSet)
router.register(r'aerolinea', views.AerolineaViewSet)
router.register(r'areaTrabajo', views.AreaTrabajoViewSet)
router.register(r'avion', views.AvionViewSet)
router.register(r'empleado', views.EmpleadoViewSet)
router.register(r'aeropuerto', views.AeropuertoViewSet)
router.register(r'viaje', views.ViajeViewSet)
router.register(r'boleto', views.BoletoViewSet)
router.register(r'ruta', views.RutaViewSet)
router.register(r'direccion', views.DireccionViewSet)
router.register(r'reservacionViajes', views.ReservacionViajesViewSet)
router.register(r'pasajero', views.PasajeroViewSet)
router.register(r'tarifa', views.TarifaViewSet)
router.register(r'pago', views.PagoViewSet)
router.register(r'asiento', views.AsientoViewSet)
router.register(r'student', views.StudentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]