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
        fields = ['nombre']
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
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['categoria', 'codigo', 'nombre', 'moneda', 'precio', 'imagen']
        widgets={
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione categoria',
                    'id': 'categoria',
                }
            ),
            'codigo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese codigo de producto',
                    'id': 'codigo',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre de producto',
                    'id': 'nombre',
                }
            ),
            'moneda': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'seleccione moneda',
                    'id': 'moneda',
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese precio',
                    'id': 'precio',
                }
            ),            
        }
