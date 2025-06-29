from django.urls import path
from usuarios_app.views.login import LoginUsuarioView
from usuarios_app.views.register_alumno import RegisterUserAV
from usuarios_app.views.datosgenerales import DatosGenerales
from django.contrib.auth.views import LogoutView
from usuarios_app.views.loginsuperuser import LoginSuperStaffView
from usuarios_app.views.change_password import ChangePasswordView 
from usuarios_app.views.docente.lista_alumnos import ListaAlumnosLV

urlpatterns = [
    path('home/datosgenerales', DatosGenerales.as_view(), name='datosgenerales'),
    path('login', LoginUsuarioView.as_view(), name='login'),
    path('panel/login', LoginSuperStaffView.as_view(), name='panel_login'),
    path('register', RegisterUserAV.as_view(), name='register'),
    path('change/password', ChangePasswordView.as_view(), name='change_password'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('docente/lista/alumnos/', ListaAlumnosLV.as_view(), name='docente_lista_alumnos'),
]