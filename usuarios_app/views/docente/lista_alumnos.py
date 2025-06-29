from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from usuarios_app.models.docente import DocenteModel

class ListaAlumnosLV(LoginRequiredMixin, DetailView):
    template_name = 'usuarios/docente/index.html'
    context_object_name = 'docente'
    model = DocenteModel
    
    def get_object(self):
        return DocenteModel.objects.get(usuario=self.request.user)
