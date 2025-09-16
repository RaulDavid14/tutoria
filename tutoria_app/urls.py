from django.urls import path
from tutoria_app.views.sesiones import (
SesionesView
,sesiones_list
,SesionTV
)
from tutoria_app.views.alumnos.lista import AlumnosLV

urlpatterns = [
    path('dashboard/sesiones', SesionesView.as_view(), name='sesiones'),
    path('docente/lista/alumnos', AlumnosLV.as_view(), name='lista_alumnos'),
    path('api/sesiones', sesiones_list, name='sesion_list'),
    path('sesion/', SesionTV.as_view(), name='sesion')
]