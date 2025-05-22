from django.contrib.auth.views import LoginView
from usuarios_app.forms.loginsuperuser import LoginFormSuperStaff

class LoginSuperStaffView(LoginView):
    authentication_form = LoginFormSuperStaff
    template_name = 'usuarios/loginsuperuser.html'
    redirect_authenticated_user = True
