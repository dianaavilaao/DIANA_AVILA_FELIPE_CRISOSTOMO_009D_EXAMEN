
from django import forms
from .models import Cliente

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),  # Para ocultar la entrada de la contraseña
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Aquí puedes añadir validaciones adicionales para la contraseña
        return password