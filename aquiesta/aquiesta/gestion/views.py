from django.shortcuts import render
# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from gestion.forms import CrearUsuarioForm
from gestion.models import Producto, Empresa, Productodetalle, Usuario, Pedido, Pedidodetalle


def pedidoproceso(request):
    return render(request, 'pedidoproceso.html')

def get_Qitems(id_usuario):
    QItems = Pedidodetalle.objects.filter(pedido__id_usuario=id_usuario).count()
    return QItems

@login_required(login_url='iniciarsesion')
def agregarproducto(request, id):
    id_user = request.user.id
    username = request.user.username
    usuario = Usuario.objects.filter(id_usuario=id_user)
    producto = Producto.objects.get(id_producto=id)
    pedido  = Pedido.objects.filter(id_usuario=id_user, empresa__id_empresa=producto.categoria.empresa.id_empresa, st_pedido='PROCESO')
    
    if not usuario:
        usuario = Usuario.objects.create(id_usuario=id_user, nombre=username)
    if not pedido:
        pedido = Pedido.objects.create(empresa=producto.categoria.empresa, id_usuario=id_user, st_pedido='PROCESO')
    pedidoitem = Pedidodetalle.objects.filter(pedido=pedido[0].id_pedido, producto=id)

    if not pedidoitem:
        pedidoitem = Pedidodetalle.objects.create(
            pedido = pedido[0], 
            producto = producto, 
            coproducto = producto.codigo, 
            descripcion = producto.nombre, 
            cantidad = 1, 
            precio = producto.precio,
        )

    context = {}
    return get_producto(request, id)

def registarusuario(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        form = CrearUsuarioForm()
        if request.method=='POST':
            form = CrearUsuarioForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                idusuario = form.cleaned_data.get('id')
                messages.success(request,'Usuario [' + str(idusuario) +'-'+ user + '] su cuenta ha sido creada')
                return redirect('iniciarsesion')
        context = {'form':form}
        return render(request, 'registrarusuario.html', context)

def cerrarsesion(request):
    logout(request)
    return redirect('inicio')

def iniciarsesion(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.info(request,'Usuario y/o contraseña incorrecta(s)')
        context = {}
        return render(request, 'iniciarsesion.html', context)

def get_producto(request, id):
    error=[]
    producto=[]
    Qitems=0
    try:
        producto = Producto.objects.get(id_producto=id)
        empresa = Empresa.objects.get(id_empresa=producto.categoria.empresa.id_empresa)
        productodetalle = Productodetalle.objects.filter(producto=producto.id_producto)
        Qitems = get_Qitems(request.user.id)
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'producto.html', { 'producto':producto, 'error': error, 'empresa':empresa, 'productodetalle': productodetalle, 'Qitems': Qitems})

class buscarProducto(ListView):
    model = Producto
    template_name = 'principal.html'
    def get_queryset(self, ):
        p_buscar = self.request.GET['producto']
        return self.model.objects.filter(nombre__icontains=p_buscar)
    def get_context_data(self, request, **kwargs):
        contexto = {}
        contexto['productos'] = self.get_queryset()
        contexto['Qitems'] = get_Qitems(request.user.id)
        return contexto
    def get(self, request,*args,**kwargs):
        return render(request, self.template_name,self.get_context_data(request))

class inicio(ListView):
    model = Producto
    template_name = 'principal.html'
    def get_queryset(self, ):
        return self.model.objects.all().order_by('-nombre', '-fecha_creacion')[:12]
    def get_context_data(self, request, **kwargs):
        contexto = {}
        contexto['productos'] = self.get_queryset()
        contexto['Qitems'] = get_Qitems(request.user.id)
        return contexto
    def get(self, request,*args,**kwargs):
        return render(request, self.template_name,self.get_context_data(request))

