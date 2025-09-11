from django.db import models
from usuarios_app.models.usuario import UsuarioModel

class DomicilioFamiliarModel(models.Model):
    usuario = models.OneToOneField(UsuarioModel, on_delete=models.CASCADE, related_name='domicilio')
    calle = models.CharField(max_length=255, null=True)
    no_ext = models.CharField(max_length=10, null=True)
    no_int = models.CharField(max_length=10, null=True, blank=True)
    cp = models.IntegerField(null=True)
    
    colonia = models.CharField(max_length=255, null=True)
    municipio = models.CharField(max_length=255, null=True)
    
    class Meta:
        db_table = 'domicilio_familiar'
        verbose_name = 'domicilio familiar'
        verbose_name_plural = 'domicilios familiares'