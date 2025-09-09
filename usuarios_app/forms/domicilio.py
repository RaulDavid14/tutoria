from django import forms
from usuarios_app.models.domicilio import DomicilioModel

atributos = {'class' : 'form-control', 'placeholder' : ''}
class DomicilioForm(forms.ModelForm):
    class Meta:
        model = DomicilioModel
        exclude = ['id']
        widgets = {
            'calle' : forms.TextInput(attrs=atributos)
            ,'no_ext' : forms.TextInput(attrs=atributos)
            ,'no_int' : forms.TextInput(attrs=atributos)
            ,'cp' : forms.TextInput(attrs=atributos)
            ,'colonia' : forms.TextInput(attrs=atributos)
            ,'municipio' : forms.TextInput(attrs=atributos)
        }