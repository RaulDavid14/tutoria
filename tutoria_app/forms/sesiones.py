from django import forms
from tutoria_app.models.sesion import SesionModel
from catalogos_app.models.motivo_sesion import CatMotivoSesionModel

class SesionesForm(forms.ModelForm):
    motivo_sesion = forms.ModelChoiceField(
        queryset=CatMotivoSesionModel.objects.all()
        ,label='Motivo de sesión'
    )
    class Meta:
        model = SesionModel
        exclude = ['alumno', 'docente', 'fecha_registro', 'fecha_respuesta', 'comentario', 'estado']
        widgets = {
            'fecha_sesion': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local', 
                }
            )
        }