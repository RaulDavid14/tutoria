from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from usuarios_app.forms.login import LoginForm


class LoginUsuarioView(LoginView):
    template_name = 'usuarios/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True
    
    def get_success_url(self):
        user = self.request.user
        
        if hasattr(user, 'cambiar_password') and user.cambiar_password: 
            return reverse_lazy('change_password')
        else:
            return reverse_lazy('home')