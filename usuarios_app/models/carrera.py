from django.db import models 
from .usuario import UsuarioModel

class CarreraModel(models.Model):
    usuario = models.OneToOneField(UsuarioModel, on_delete=models.CASCADE)   
    
    
    class Meta:
        db_table = 'carrera'
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'