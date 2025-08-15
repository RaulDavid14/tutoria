from usuarios_app.models.docente import DocenteModel
from django.views.generic import ListView
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from panel_app.forms.register_docente import RegisterDocenteForm

class DocenteLV(ListView):
    model = DocenteModel
    context_object_name = 'docentes'
    template_name = 'panel/docente/list.html'
    paginate_by = 10
    

    def get_queryset(self):
        return DocenteModel.objects.all().order_by('id')
   