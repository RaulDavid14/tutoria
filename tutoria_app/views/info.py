from django.views.generic import DetailView
from usuarios_app.models.alumno import AlumnoModel

class InfoDocenteDV(DetailView):
    model = AlumnoModel
    template_name = 'sesiones/informacion_docente'
    context_object_name = 'docente'
    
    