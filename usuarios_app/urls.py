from django.urls import path
from usuarios_app.views.login import LoginUsuarioView
from usuarios_app.views.register import RegisterUserAV
from usuarios_app.views.datosgenerales import DatosGenerales
from django.contrib.auth.views import LogoutView
from usuarios_app.views.loginsuperuser import LoginSuperStaffView

urlpatterns = [
    path('datosgenerales', DatosGenerales.as_view(), name='datosgenerales'),
    path('login', LoginUsuarioView.as_view(), name='login'),
    path('panel/login', LoginSuperStaffView.as_view(), name='panel_login'),
    path('register', RegisterUserAV.as_view(), name='register'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
]