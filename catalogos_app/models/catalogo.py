from django.db import models

class CatalogoModel(models.Model):
    nombre = models.CharField(max_length=50)
    abreviacion = models.CharField(max_length=5)
    descripcion = models.TextField(blank=True, null=True)
        
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True