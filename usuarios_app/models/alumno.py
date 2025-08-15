from django.db import models
from .usuario import UsuarioModel
from usuarios_app.models.docente import DocenteModel

class AlumnoModel(models.Model):
    usuario = models.OneToOneField(UsuarioModel, on_delete = models.CASCADE, related_name='alumno')
    programa_educativo = models.CharField(max_length=255, null=True)
    ingreso = models.CharField(max_length=6, null=True)                     #ciclo escolar
    tiene_tutor = models.BooleanField(default=False)
    tutor = models.ForeignKey(DocenteModel, on_delete=models.CASCADE,related_name='alumnos', null=True)
    
    
    class Meta:
        db_table = 'alumnos'
        verbose_name = 'alumno'
        verbose_name_plural = 'Alumnos'
    
    def __str__(self):
        return str(self.usuario.codigo)