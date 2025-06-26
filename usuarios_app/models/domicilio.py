from django.db import models
from .usuario import UsuarioModel
from usuarios_app.managers.domicilio import DomicilioManager

class DomicilioModel(models.Model):
    usuario = models.OneToOneField(UsuarioModel, on_delete=models.CASCADE, related_name='domicilio')
    calle = models.CharField(max_length=255)
    no_ext = models.IntegerField()
    no_int = models.IntegerField(null=True, blank=True)
    cp = models.models.IntegerField()
    
    colonia = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    
    objects = DomicilioManager()
    
    class Meta:
        db_table = 'domicilio'
        verbose_name = 'Domicilio'
        verbose_name_plural = 'Domiclios'