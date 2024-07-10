
from django import forms
from .models import Cliente, Producto

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
    
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio_con_descuento', 'precio_normal', 'imagen', 'tipo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_con_descuento': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_normal': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
        }