""" from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CrearUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

 """

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CrearUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2', 'is_staff']
