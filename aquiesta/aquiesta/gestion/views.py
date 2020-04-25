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
from gestion.models import Producto, Empresa, Productodetalle, Usuario, Pedido

@login_required(login_url='iniciarsesion')
def agregarproducto(request, id):
    id_user = request.user.id
    username = request.user.username
    usuario = Usuario.objects.filter(id_usuario=id_user)
    pedido  = Pedido.objects.filter(id_usuario=id_user, st_pedido='PROCESO')
    producto = Producto.objects.get(id_producto=id)

    if not usuario:
        usuario = Usuario.objects.create(id_usuario=id_user, nombre=username)
        usuario.save()
    if not pedido:
        pedido = Pedido.objects.create(empresa=producto.categoria.empresa, id_usuario=id_user, st_pedido='PROCESO')
        print('NO existe pedido')

    context = {}
    return get_producto(request, id)

""" 
    fec_emision = models.DateTimeField(blank=True, null=True)
    tipo_doc_iden = models.CharField(max_length=1, blank=True, null=True)
    num_doc_iden = models.CharField(max_length=15, blank=True, null=True)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    ubigeo = models.ForeignKey('Ubigeo', models.DO_NOTHING, db_column='id_ubigeo', blank=True, null=True)
    telefono = models.CharField(max_length=200, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    entrega_domicilio = models.BooleanField(default=False)
    costo_entrega = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cancelado = models.BooleanField(default=False)
 """

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
                print(user + ' ' + str(idusuario))
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
    try:
        producto = Producto.objects.get(id_producto=id)
        empresa = Empresa.objects.get(id_empresa=producto.categoria.empresa.id_empresa)
        productodetalle = Productodetalle.objects.filter(producto=producto.id_producto)
        print(productodetalle)
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'producto.html', { 'producto':producto, 'error': error, 'empresa':empresa, 'productodetalle': productodetalle})

class buscarProducto(ListView):
    model = Producto
    template_name = 'principal.html'
    def get_queryset(self, ):
        p_buscar = self.request.GET['producto']
        return self.model.objects.filter(nombre__icontains=p_buscar)
    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['productos'] = self.get_queryset()
        return contexto
    def get(self, request,*args,**kwargs):
        return render(request, self.template_name,self.get_context_data())

class inicio(ListView):
    model = Producto
    template_name = 'principal.html'
    def get_queryset(self, ):
        return self.model.objects.all().order_by('-nombre', '-fecha_creacion')[:12]
    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['productos'] = self.get_queryset()
        return contexto
    def get(self, request,*args,**kwargs):
        return render(request, self.template_name,self.get_context_data())

