from django.views.generic import FormView
from usuarios_app.forms.register import RegisterForm

class RegisterForm(FormView):
    template_name = 'usuarios/login.html'
    success_url = 'login'
    form_class = RegisterForm
    
    def form_valid(self, form):
        
        return super().form_valid(form)
    