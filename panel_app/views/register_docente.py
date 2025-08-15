from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from panel_app.forms.register_docente import RegisterDocenteForm
from usuarios_app.models.docente import DocenteModel
from django.contrib import messages

class RegisterDocenteCV(CreateView):
    template_name = 'panel/register_docente.html'
    success_url = reverse_lazy('register_docente')
    form_class = RegisterDocenteForm

    def form_valid(self, form):
        try:
            usuario = form.save(commit=False)
            usuario.rol = 'tutor'
            usuario.cambiar_password = True
            usuario.save()
            DocenteModel.objects.create(usuario = usuario)

            messages.success(self.request, 'Se ha dado de alta con éxito')
            return redirect(self.success_url)
        except Exception as exception:
            messages.error(self.request, f'Error inesperado {str(exception)}')
            return self.form_invalid(form)