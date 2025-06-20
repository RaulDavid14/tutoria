from django.db import models
from usuarios_app.models.usuario import UsuarioModel

class DocenteModel(models.Model):
    usuario = models.OneToOneField(UsuarioModel, on_delete=models.CASCADE)
    programa_educativo = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'docentes'
        verbose_name = 'docente'
        verbose_name_plural = 'Docentes'
        
    def __str__(self):
        return self.usuario.email