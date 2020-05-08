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

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['tipo_doc_ident','num_doc_ident','nombre','direccion','ubigeo','telefono','imagen']
        widgets={
            'tipo_doc_ident': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'tipo_doc_ident',
                }
            ),
            'num_doc_ident': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'num_doc_ident',
                }
            ),            
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'nombre',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'direccion',
                }
            ),
            'ubigeo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'ubigeo',
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'telefono',
                }
            ),

        }
    
class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['ruc', 'rznsocial', 'direccion', 'telefono', 'ubigeo', 'imagen', 'logo']
        widgets = {
            'ruc': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'ruc',
                }
            ),
            'rznsocial': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'rznsocial',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'direccion',
                }
            ),
            'ubigeo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'ubigeo',
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'telefono',
                }
            ),
        }

