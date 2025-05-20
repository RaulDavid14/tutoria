from django.urls import path
from usuarios_app.views.login import LoginUsuarioView
from usuarios_app.views.register import RegisterForm

urlpatterns = [
    path('login', LoginUsuarioView.as_view(), name='login'),
    path('register', RegisterForm.as_view(), name='register'),
]