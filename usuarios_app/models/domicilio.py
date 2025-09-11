from django.db import models
from .usuario import UsuarioModel
from usuarios_app.managers.domicilio import DomicilioManager

class DomicilioModel(models.Model):
    usuario = models.OneToOneField(UsuarioModel, on_delete=models.CASCADE, related_name='domicilio')
    calle = models.CharField(max_length=255, null=True)
    no_ext = models.CharField(max_length=10, null=True)
    no_int = models.CharField(max_length=10, null=True, blank=True)
    cp = models.IntegerField(null=True)
    
    colonia = models.CharField(max_length=255, null=True)
    municipio = models.CharField(max_length=255, null=True)
    
    objects = DomicilioManager()
    
    class Meta:
        db_table = 'domicilio'
        verbose_name = 'Domicilio'
        verbose_name_plural = 'Domiclios'
    
    def __str__(self):
        return f'domicilio de {self.usuario.email}'