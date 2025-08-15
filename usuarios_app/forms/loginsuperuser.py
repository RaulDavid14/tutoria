from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import authenticate

class LoginFormSuperStaff(AuthenticationForm):
    username = forms.EmailField(
        label='Correo Electrónicos'
        ,widget=forms.EmailInput(attrs={
            'class' : 'form-control'
            ,'placeholder' : ''
    }))
    
    password = forms.CharField(
        label='Contraseña'
        ,widget=forms.PasswordInput(attrs={
        'class' : 'form-control'
        ,'placeholder' : ''
    }))
    
    def confirm_login_allowed(self, user):
        if not (user.is_active and (user.is_superuser or user.is_staff)):
            raise forms.ValidationError(
                "Solo usuarios superusuario o staff pueden iniciar sesión.",
                code='no_permiso',
            )
