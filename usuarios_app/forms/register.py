from django import forms
from usuarios_app.models.usuario import UsuarioModel

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'class' : 'form-control'
            ,'placeholder' : ''
        }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control'
        ,'placeholder' : ''
    }))
    
    class Meta:
        model = UsuarioModel
        fields = ['codigo', 'email']
        widgets = {
            'codigo': forms.NumberInput(attrs={
                'class': 'form-control'
                ,'placeholder' : ''
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
                ,'placeholder' : ''
            }),
        }