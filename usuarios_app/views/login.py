from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from usuarios_app.forms.login import LoginForm


class LoginUsuarioView(LoginView):
    template_name = 'usuarios/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')