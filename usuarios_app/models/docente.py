from django.db import models
from usuarios_app.models.usuario import UsuarioModel

class DocenteModel(models.Model):
    usuario = models.OneToOneField(UsuarioModel, on_delete=models.CASCADE)
    