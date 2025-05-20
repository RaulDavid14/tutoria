from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from usuarios_app.managers.usuario import UsuarioManager

class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    codigo = models.BigIntegerField()
    nombres = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=60)
    apellido_materno = models.CharField(max_length=60, null=True,blank=True)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    estado_civil = models.CharField(verbose_name=10, null=True)
    celular = models.BigIntegerField()
    telefono = models.BigIntegerField(null=True, blank=True)
    
    rol = models.CharField(max_length=14)
    
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    
    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'nombres', 
        'apellido_paterno', 
        'rol'
    ]
    
    objects = UsuarioManager()
    
    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'