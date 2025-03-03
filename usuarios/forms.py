from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioPersonalizado  # Asegúrate de importar tu modelo de usuario

class RegistroForm(UserCreationForm):
    telefono = forms.CharField(max_length=15, required=True, label="Teléfono")

    class Meta:
        model = UsuarioPersonalizado  # Usa tu modelo personalizado
        fields = ['username', 'email', 'telefono', 'password1', 'password2']