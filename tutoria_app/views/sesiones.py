from django.views.generic import CreateView
from tutoria_app.forms.sesiones import SesionesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, get_object_or_404

from usuarios_app.models.alumno import AlumnoModel

class SesionesCV(LoginRequiredMixin, CreateView):
    template_name = 'sesiones/index.html'
    form_class = SesionesForm

class SesionesView(View):
    
    def get(self, request):
        alumno = get_object_or_404(AlumnoModel, usuario = request.user)
        tutor = alumno.tutor
        
        context = {
            'alumno' :  alumno,
            'tutor' : tutor
        }
        return render(request, 'sesiones/index.html', context=context)