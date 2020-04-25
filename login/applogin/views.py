from django.shortcuts import render
# Create your views here.
from django.shortcuts import redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CrearUserForm
from .filters import *

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CrearUserForm()
        if request.method=='POST':
            form = CrearUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'La cuenta fue creada para ' + user)

                return redirect('login')
        context = {'form': form}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Usuario y/o contraseña incorrecta(s)')
        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


""" @login_required(login_url='login') """
def home(request):
    context = {}
    return render(request,'home.html', context)

@login_required(login_url='login')
def producto(request):
    context = {}
    return render(request,'producto.html', context)
