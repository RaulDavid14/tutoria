from django import forms
from usuarios_app.models.usuario import UsuarioModel
from usuarios_app.models.docente import DocenteModel
from django.utils import timezone

atributos = {'class' : 'form-control', 'placeholder' : ''}
class RegisterDocenteForm(forms.ModelForm):
    
    #Perzonalizar en caso de querer validaciones extras.
    def save(self, commit=True):
        docente = super().save(commit=False)
        docente.set_password(f'UdeG{timezone.now().year}')
        
        if commit:
            docente.save()
        return docente
    class Meta:
        model = UsuarioModel
        fields = ['codigo','nombres','apellido_paterno','apellido_materno','email','celular','telefono']
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
    