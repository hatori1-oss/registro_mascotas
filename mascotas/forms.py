from django import forms
from .models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'color', 'raza', 'edad', 'foto']


class RegistroUsuario(forms.Form):
    nombre = forms.CharField(max_length = 100)
    email = forms.EmailField()
