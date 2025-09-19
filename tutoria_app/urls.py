from django.urls import path
from tutoria_app.views.sesiones import (
sesiones_list
,SesionCV
)
from tutoria_app.views.alumnos.lista import AlumnosLV

urlpatterns = [
    path('docente/lista/alumnos', AlumnosLV.as_view(), name='lista_alumnos'),
    path('api/sesiones', sesiones_list, name='sesion_list'),
    path('dashboard/sesion/', SesionCV.as_view(), name='sesion'),
]