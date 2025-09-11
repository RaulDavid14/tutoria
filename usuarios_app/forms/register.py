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
        
    #Hacer validaciones adicionales sobre los campos
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Las contraseñas no coinciden")

    #Realizar alguna accion antes de guardar el objeto.
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        user.set_password(password)  
        if commit:
            user.save()
        return user