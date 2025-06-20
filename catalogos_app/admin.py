from django.contrib import admin
from .models.motivo_sesion import CatMotivoSesionModel
from .models.programaeducativo import CatProgramaEducativoModel
# Register your models here.

admin.site.register(CatMotivoSesionModel)
admin.site.register(CatProgramaEducativoModel)