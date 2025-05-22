from django.db import models
from usuarios_app.models.usuario import UsuarioModel

class DatosSocioeconomicosModel(models.Model):
    usuario = models.OneToOneField(UsuarioModel, on_delete=models.CASCADE)
    trabaja = models.BooleanField(default=False)
    nombre_trabajo = models.CharField(max_length=100)
    apoyo_economico = models.BooleanField(default=True)
        
    
    class Meta:
        db_table = 'datos_socioeconomicos'
        verbose_name = 'Dato socioeconomico'
        verbose_name_plural = 'Datos socioeconomicos'
    