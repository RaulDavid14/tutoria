from django.views.generic import CreateView
from tutoria_app.forms.sesiones import SesionesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect

from usuarios_app.models.alumno import AlumnoModel
from usuarios_app.models.docente import DocenteModel

class SesionesCV(LoginRequiredMixin, CreateView):
    template_name = 'sesiones/index.html'
    form_class = SesionesForm

class SesionesView(View):

    def get_context(self, request):
        alumno = get_object_or_404(AlumnoModel, usuario=request.user)
        lista_sesiones = alumno.sesiones.all()        
        tutor = alumno.tutor
        sesiones = SesionesForm()
        return {
            'alumno': alumno,
            'tutor': tutor,
            'sesiones': sesiones,
            'lista_sesiones' : lista_sesiones
        }

    def get(self, request):
        context = self.get_context(request)
        return render(request, 'sesiones/index.html', context)

    def post(self, request):
        form = SesionesForm(request.POST)
        print(f'contenido {form}')

        if form.is_valid():
            nueva_sesion = form.save(commit=False)
            nueva_sesion.alumno = get_object_or_404(AlumnoModel, usuario=request.user)
            print(f'valor {nueva_sesion.alumno}')
            nueva_sesion.docente = nueva_sesion.alumno.tutor
            nueva_sesion.save()
            return redirect('sesion')  

        context = self.get_context(request)
        context['sesiones'] = form  
        return render(request, 'sesiones/index.html', context)