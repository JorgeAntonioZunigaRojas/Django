from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from gestion.models import *

class CrearUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['id','username', 'email', 'password1', 'password2']


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['empresa', 'nombre']
        label={
            'nombre':'Nombre',
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre de categoria',
                    'id': 'nombre',
                }
            ),
            'empresa': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese ID de empresa',
                    'id': 'empresa',
                }
            ),
        }
