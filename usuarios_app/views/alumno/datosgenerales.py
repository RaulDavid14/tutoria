from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from usuarios_app.forms.datosgenerales import DatosGeneralesForm
from usuarios_app.models import UsuarioModel
from django.contrib import messages

class DatosGenerales(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    template_name = 'usuarios/datos_generales.html'
    form_class = DatosGeneralesForm
    
    #Obtiene el objeto a actualizar. 
    def get_object(self):
        usuario = UsuarioModel.objects.get_user(self.request.user.email, self.request.user.codigo)
        print(f'valor encontrado: {usuario}')
        return usuario
    
    def form_valid(self, form):
        print("form_valid() llamado")
        print("cleaned_data:", form.cleaned_data)
        messages.success(self.request, "Tus datos han sido actualizados")
        response = super().form_valid(form)
        
        return response
    
    def form_invalid(self, form):
        print("form_invalid() llamado")
        print("Errores:", form.errors)
        messages.error(self.request, 'Error al actualizar tus datos')
        
        return super().form_invalid(form)
    
    #redirige a la misma ruta
    def get_success_url(self):
        return self.request.path