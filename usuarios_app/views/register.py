from django.views.generic import CreateView
from usuarios_app.forms.register import RegisterForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from usuarios_app.models.alumno import AlumnoModel

class RegisterUserAV(CreateView):
    template_name = 'usuarios/register.html'
    success_url = reverse_lazy('login')
    form_class = RegisterForm
    
    def form_valid(self, form):
        usuario = form.save(commit=False)
        usuario.rol = 'estudiante'
        usuario.save()

        AlumnoModel.objects.create(usuario=usuario)
        return redirect(self.success_url)