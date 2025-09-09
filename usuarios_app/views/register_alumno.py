from django.views.generic import CreateView
from usuarios_app.forms.register import RegisterForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from usuarios_app.models.alumno import AlumnoModel
from usuarios_app.models.domicilio import DomicilioModel
from django.contrib import messages

class RegisterUserAV(CreateView):
    template_name = 'usuarios/register.html'
    success_url = reverse_lazy('login')
    form_class = RegisterForm
    
    def form_valid(self, form):
        try:
            usuario = form.save(commit=False)
            usuario.rol = 'estudiante'
            usuario.save()

            AlumnoModel.objects.create(usuario=usuario)
            DomicilioModel.objects.create(usuario=usuario)
            
            print('usuario creado con éxito.')
            
            return redirect(self.success_url)
        except Exception as exception:
            messages.error(self.request, f'Error inesperado {str(exception)}')
            return self.form_invalid(form)