from django.db import models
from usuarios_app.models.alumno import AlumnoModel
from usuarios_app.models.docente import DocenteModel
from tutoria_app.managers.sesion import SesionManager

class SesionModel(models.Model):
    alumno = models.ForeignKey(AlumnoModel, on_delete=models.CASCADE, related_name='sesiones')
    docente = models.ForeignKey(DocenteModel, on_delete=models.CASCADE, related_name='sesiones')
    
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aceptada', 'Aceptada'),
        ('cancelada', 'Cancelada'),
        ('rechazada', 'Rechazada'),
    ]
    
    motivo_sesion = models.CharField(null=True,  max_length=255)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')
    comentario = models.TextField(null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_respuesta = models.DateTimeField(null=True)
    fecha_sesion = models.DateTimeField()
    objects = SesionManager()
    
    class Meta:
        db_table = 'sesiones'
        verbose_name = 'Sesión'
        verbose_name_plural = 'Sesiones'
    
    def __str__(self):
        return f'{self.id} {self.alumno.usuario.email}'