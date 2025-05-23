from django.contrib.auth.views import LoginView
from usuarios_app.forms.loginsuperuser import LoginFormSuperStaff
from django.urls import reverse_lazy

class LoginSuperStaffView(LoginView):
    authentication_form = LoginFormSuperStaff
    template_name = 'usuarios/loginsuperuser.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard_panel')