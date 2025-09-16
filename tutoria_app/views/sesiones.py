from tutoria_app.forms.sesiones import SesionesForm, SesionModel
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from usuarios_app.models.alumno import AlumnoModel
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from tutoria_app.api.sesionrequest import SesionRequestSerializer
from tutoria_app.api.sesion import SesionSerializer

class SesionTV(LoginRequiredMixin, TemplateView):
    template_name = 'sesiones/lista_sesiones.html'

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def sesiones_list(request):
    print('sesiones_list()')
    print(f'request.user {request.user}')
    
    serializer = SesionRequestSerializer(data=request.GET)
    serializer.is_valid(raise_exception=True)
    filters = serializer.validated_data

    filters['order'] = filters['order'] if 'order' in filters else 'id'
    queryset = SesionModel.objects.sesionesFind(filters, request.user)

    paginator = PageNumberPagination()
    
    paginator.page_size = filters['size'] if 'size' in filters and filters['size'] > 0 else 5
    page = paginator.paginate_queryset(queryset, request)
    
    return paginator.get_paginated_response(SesionSerializer(page, many=True).data)


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