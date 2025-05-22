from django import forms
from usuarios_app.models.usuario import UsuarioModel

atributos = {'class' : 'form-control', 'placeholder' : ''}
class DatosGeneralesForm(forms.ModelForm):
    carrera = forms.CharField(widget=forms.TextInput(attrs=atributos))
    class Meta:
        model = UsuarioModel
        exclude = ['id'
                   , 'rol'
                   , 'fecha_creacion'
                   , 'fecha_actualizacion'
                   ,'is_staff'
                   ,'is_active'
                ]
        widgets = {
            'codigo' : forms.NumberInput(attrs=atributos)
            
            ,'nombres' : forms.TextInput(attrs={
                'class' : 'form-control', 'placeholder' : ''
            })
            ,'email' : forms.EmailInput(attrs={
                'class' : 'form-control', 'placeholder' : '', 'type' : 'email'
            })
            ,'apellido_paterno' : forms.TextInput(attrs=atributos)
            ,'apellido_materno' : forms.TextInput(attrs=atributos)
            ,'fecha_nacimiento' : forms.DateInput(attrs={
                'class' : 'form-control', 'placeholder' : '', 'type' : 'date'       
            })
            ,'estado_civil' : forms.TextInput(attrs=atributos)
            ,'celular' : forms.NumberInput(attrs=atributos)
            ,'telefono' : forms.NumberInput(attrs=atributos)
        }