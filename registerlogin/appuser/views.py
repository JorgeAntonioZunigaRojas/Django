from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from appuser.forms import CrearUsuarioForm

def iniciarsesion(request):
    if request.user.is_authenticated:
        return redirect('principal')
    else:
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('principal')
            else:
                messages.info(request, 'Usuario y/o contraseña incorrecta(s).')
        context = {}
        return render(request, 'iniciarsesion.html', context) 

def cerrarsesion(request):
    logout(request)
    return redirect('iniciarsesion')

def registro(request):
    if request.user.is_authenticated:
        return redirect('principal')
    else:
        form = CrearUsuarioForm()
        if request.method=='POST':
            form = CrearUsuarioForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'La cuenta fue creada para '+ user)
                return redirect('iniciarsesion')

        context = {'form':form}
        return render(request, 'registro.html', context)

    


def principal(request):
    contexto = {}
    return render(request, 'principal.html', contexto)

@login_required(login_url='iniciarsesion')
def producto(request):
    contexto = {}
    return render(request, 'producto.html', contexto)

@login_required(login_url='iniciarsesion')
def cliente(request):
    contexto = {}
    return render(request, 'cliente.html', contexto)
