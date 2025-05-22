from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from usuarios_app.forms.datosgenerales import DatosGeneralesForm
from usuarios_app.models import UsuarioModel

class DatosGenerales(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    template_name = 'usuarios/datos_generales.html'
    form_class = DatosGeneralesForm
    
    def get_object(self):
        email = self.request.user.email
        codigo = self.request.user.codigo
        return UsuarioModel.objects.get_user(email, codigo)
    
    #redirige a la misma ruta
    def get_success_url(self):
        return self.request.path