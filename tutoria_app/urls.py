from django.urls import path
from tutoria_app.views.sesiones import SesionesView
from tutoria_app.views.alumnos.lista import AlumnosLV

urlpatterns = [
    path('dashboard/sesiones', SesionesView.as_view(), name='sesion'),
    path('docente/lista/alumnos', AlumnosLV.as_view(), name='lista_alumnos'),
]