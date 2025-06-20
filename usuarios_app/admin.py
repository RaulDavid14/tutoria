from django.contrib import admin
from .models.usuario import UsuarioModel
from .models.alumno import AlumnoModel
from .models.docente import DocenteModel

# Register your models here.
admin.site.register(AlumnoModel)
admin.site.register(UsuarioModel)
admin.site.register(DocenteModel)