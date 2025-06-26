from django.urls import path
from tutoria_app.views.sesiones import SesionesCV

urlpatterns = [
    path('registro/sesion', SesionesCV.as_view(), name='registro_sesion'),
]
