from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from usuarios_app.managers.usuario import UsuarioManager

class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    codigo = models.BigIntegerField(null=True, unique=True)
    nombres = models.CharField(max_length=255, null=True)
    apellido_paterno = models.CharField(max_length=60, null=True)
    apellido_materno = models.CharField(max_length=60, null=True,blank=True)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField(null=True)
    estado_civil = models.CharField(verbose_name=10, null=True)
    celular = models.BigIntegerField(null=True)
    telefono = models.BigIntegerField(null=True, blank=True)
    cambiar_password = models.BooleanField(default=False)
    
    ROLE_CHOICES = [
        ('estudiante', 'Estudiante'),
        ('tutor', 'Tutor'),
        ('admin', 'Administrador'),
    ]
    
    rol = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True) 
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    
    objects = UsuarioManager()
    
    class Meta:
        db_table = 'usuarios'
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
    
    def nombre_completo(self):
        nombres = self.nombres if self.nombres else 'sin nombre'
        apellido_paterno = self.apellido_paterno if self.apellido_paterno else 'sin apellido paterno'
        apellido_materno = self.apellido_materno if self.apellido_materno else 'sin apellido materno'
        return f'{apellido_paterno} {apellido_materno} {nombres}'
    
    def __str__(self):
        return f'{self.email} rol {self.rol}'