from tutoria_app.forms.sesiones import SesionesForm, SesionModel
from django.views import View
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from usuarios_app.models.alumno import AlumnoModel
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from tutoria_app.api.sesionrequest import SesionRequestSerializer
from tutoria_app.api.sesion import SesionSerializer

"""
    TODO:
    - modificar el endpoint para que retorne el correo del alumno como parametro.
    - agregar la modal para asignar sesión dependiendo del perfil del usuario.
    - crear vista para ver detalle de sesion.
    - agregar los filtros a las tablas (revisar perfiles para solo mostrar acorde al perfil).
"""

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def sesiones_list(request):
    print('sesiones_list()')
    
    serializer = SesionRequestSerializer(data=request.GET)
    serializer.is_valid(raise_exception=True)
    filters = serializer.validated_data

    filters['order'] = filters['order'] if 'order' in filters else 'id'
    queryset = SesionModel.objects.sesionesFind(filters, request.user)

    paginator = PageNumberPagination()
    
    paginator.page_size = filters['size'] if 'size' in filters and filters['size'] > 0 else 5
    page = paginator.paginate_queryset(queryset, request)
    
    return paginator.get_paginated_response(SesionSerializer(page, many=True).data)

class SesionCV(CreateView):
    template_name = 'sesiones/lista_sesiones.html'
    form_class = SesionesForm
    success_url = reverse_lazy('sesion')
    
    def form_valid(self, form):
        print(f'form_valid() - valor de usuario {self.request.user.rol}')
        if self.request.user.rol == 'estudiante':
            alumno = AlumnoModel.objects.get(usuario=self.request.user)
            form.instance.alumno = alumno
            form.instance.docente = alumno.tutor
            print('form_valid() - sesion creada')
            return super().form_valid(form)
        else:
            return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        print(f'get_context_data() - valor de usuario {self.request.user.rol}')
        context = super().get_context_data(**kwargs)

        if self.request.user.rol == 'estudiante':
            alumno = AlumnoModel.objects.get(usuario = self.request.user)
            context['alumno'] = alumno
            context['tutor'] = alumno.tutor
            context['datos'] =  alumno.usuario

        return context
