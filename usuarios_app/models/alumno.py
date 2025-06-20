from django.db import models
from .usuario import UsuarioModel


class AlumnoModel(models.Model):
    usuario = models.OneToOneField(UsuarioModel, on_delete = models.CASCADE)
    programa_educativo = models.CharField(max_length=255, null=True)
    ingreso = models.CharField(max_length=6, null=True)    
    
    class Meta:
        db_table = 'alumnos'
        verbose_name = 'alumno'
        verbose_name_plural = 'Alumnos'
    
    def __str__(self):
        return self.usuario.email