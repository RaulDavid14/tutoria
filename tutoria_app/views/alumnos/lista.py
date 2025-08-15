from django.views.generic import ListView
from usuarios_app.models.alumno import AlumnoModel
from django.contrib.auth.mixins import LoginRequiredMixin#, UserPassesTestMixin

class AlumnosLV(LoginRequiredMixin, ListView):
    model = AlumnoModel
    template_name = 'usuarios/alumnos/index.html'
    context_object_name = 'alumnos'
    paginate_by = 10

    def get_queryset(self):
        try:
            docente = self.request.user.datos  
            return AlumnoModel.objects.filter(tutor=docente).order_by('id')
        except:
            return AlumnoModel.objects.none()  
