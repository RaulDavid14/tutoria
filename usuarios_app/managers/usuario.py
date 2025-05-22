from django.contrib.auth.models import BaseUserManager

class UsuarioManager(BaseUserManager):
    def get_user(self, email, codigo):
        return self.get(email=email, codigo=codigo)