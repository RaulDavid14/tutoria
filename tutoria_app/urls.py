from django.urls import path
from tutoria_app.views.sesiones import SesionesCV, SesionesView

urlpatterns = [
    path('sesion', SesionesView.as_view(), name='sesion'),
    #path('registro/sesion', SesionesCV.as_view(), name='registro_sesion'),
]
