from django.db import models
from usuarios_app.models.alumno import AlumnoModel
from usuarios_app.models.docente import DocenteModel
from tutoria_app.managers.sesion import SesionManager

class SesionModel():
    alumno = models.ForeignKey(AlumnoModel, on_delete=models.CASCADE)
    docente = models.ForeignKey(DocenteModel, on_delete=models.CASCADE)
    
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada'),
    ]
    
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')
    comentario = models.TextField(blank=True, null=True)
    fecha_sesion = models.DateTimeField(auto_now=True)
    fecha_respuesta = models.DateTimeField()
    
    objects = SesionManager()
    
    class Meta:
        db_table = 'sesiones'
        verbose_name = 'Sesión'
        verbose_name_plural = 'Sesiones'