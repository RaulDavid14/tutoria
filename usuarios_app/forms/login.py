from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
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
     