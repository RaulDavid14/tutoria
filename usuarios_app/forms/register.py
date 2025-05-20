from django import forms
from usuarios_app.models.usuario import UsuarioModel

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UsuarioModel
        exclude = ['id']
        