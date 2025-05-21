from django.urls import path
from usuarios_app.views.login import LoginUsuarioView
from usuarios_app.views.register import RegisterUserAV
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', LoginUsuarioView.as_view(), name='login'),
    path('register', RegisterUserAV.as_view(), name='register'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
]