from django.shortcuts import render
# Create your views here.

from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView, CreateView, View, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from gestion.forms import CrearUsuarioForm, CategoriaForm
from gestion.models import Producto, Empresa, Productodetalle, Usuario, Pedido, Pedidodetalle, Categoria



@login_required(login_url='iniciarsesionempresa')
def sis_producto_eliminar(request, id):
    producto = Producto.objects.get(id_producto=id)
    contexto = get_contexto(request)
    contexto['producto'] = producto
    if request.method=='POST':
        producto.delete()
        return redirect('sisproductolista')
    return render(request, 'producto_confirm_delete.html', contexto)

@login_required(login_url='iniciarsesionempresa')
def sis_producto_lista(request):
    contexto = get_contexto(request)
    id_empresa = contexto['id_empresa']
    contexto['productos'] = Producto.objects.filter(categoria__empresa__id_empresa=id_empresa).values('id_producto', 'codigo', 'nombre', 'categoria__nombre', 'moneda__abreviatura', 'precio', 'imagen')
    return render(request, 'sis_producto_lista.html', contexto)

@login_required(login_url='iniciarsesionempresa')
def sis_categoria_eliminar(request, id):
    categoria = Categoria.objects.get(id_categoria=id)
    contexto = get_contexto(request)
    contexto['categoria'] = categoria
    if request.method=='POST':
        categoria.delete()
        return redirect('siscategoria')
    return render(request,'categoria_confirm_delete.html', contexto)

@login_required(login_url='iniciarsesionempresa')
def sis_categoria_editar(request, id):
    error = []
    categoria_form = []
    try:
        categoria=Categoria.objects.get(id_categoria=id)
        if request.method == 'GET':
            categoria_form = CategoriaForm(instance=categoria)
        else:
            categoria_form = CategoriaForm(request.POST, instance=categoria)
            if categoria_form.is_valid():
                categoria_form.save()
                return redirect('siscategoria')
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'sis_categoria_editar.html', {'form':categoria_form, 'id_categoria': id, 'error': error})


@login_required(login_url='iniciarsesionempresa')
def sis_categoria_crear(request):
    categoria_form = CategoriaForm()
    if request.method=='POST':
        contexto = get_contexto(request)
        empresa = contexto['empresa']
        ca_nombre = request.POST.get('nombre')
        categoria_form = Categoria(empresa=empresa, nombre=ca_nombre)
        categoria_form.save()
        return redirect('siscategoria')
    return render(request, 'sis_categoria_crear.html', {'form': categoria_form})



@login_required(login_url='iniciarsesionempresa')
def sis_categoria_lista(request):
    contexto = get_contexto(request)
    empresa = contexto['empresa']
    contexto['categorias'] = Categoria.objects.filter(empresa__id_empresa=empresa.id_empresa).order_by('nombre')
    return render(request, 'sis_categoria_lista.html', contexto)

@login_required(login_url='iniciarsesionempresa')
def sisCerrarSesion(request):
    logout(request)
    return redirect('iniciarsesionempresa')

def get_contexto(request):
    contexto = {}
    id_user = request.user.id
    empresa = Empresa.objects.get(usuario__id_usuario=id_user)
    usuario = Usuario.objects.get(id_usuario=id_user)
    id_empresa = empresa.id_empresa
    contexto['empresa'] = empresa
    contexto['usuario'] = usuario
    contexto['id_empresa'] = id_empresa
    return contexto

@login_required(login_url='iniciarsesionempresa')
def sisInicio(request):
    contexto = get_contexto(request)
    id_user = request.user.id
    empresa = contexto['empresa']
    id_empresa = empresa.id_empresa
    QPxDespachar = Pedido.objects.filter(empresa__id_empresa=id_empresa, st_pedido='COMPRADO').count()
    QPEntregados = Pedido.objects.filter(empresa__id_empresa=id_empresa, st_pedido='ENTREGADO').count()
    QPEmitidos = Pedido.objects.filter(empresa__id_empresa=id_empresa).exclude(st_pedido='PROCESO').count()
    QCategorias = Categoria.objects.filter(empresa__id_empresa=id_empresa).count()
    QProductos = Producto.objects.filter(categoria__empresa__id_empresa=id_empresa).count()
    contexto['QPxDespachar'] = QPxDespachar
    contexto['QPEntregados'] = QPEntregados
    contexto['QPEmitidos'] = QPEmitidos
    contexto['QCategorias'] = QCategorias
    contexto['QProductos'] = QProductos

    return render(request, 'sis_inicio.html', contexto)

def iniciarsesionempresa(request):
    if request.user.is_authenticated:
        return redirect('sisinicio')
    else:
        if request.method=='POST':
            empresaruc = request.POST.get('empresaruc')
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                empresa = Empresa.objects.filter(ruc=empresaruc)
                if empresa:
                    if user.id==empresa[0].usuario.id_usuario:
                        login(request, user)
                        return redirect('sisinicio')
                    else:
                        messages.info(request,'RUC y/o Usuario incorecto(s)')
                else:
                    messages.info(request,'RUC NO esta registrado')
            else:
                messages.info(request,'Usuario y/o contraseña incorrecta(s)')
            
        context = {}
        return render(request, 'iniciarsesionempresa.html', context)

@login_required(login_url='iniciarsesion')
def confirmarcompra(request, id):
    pedido = Pedido.objects.get(id_pedido=id)
    pedido.st_pedido='COMPRADO'
    pedido.save()
    return redirect('pedidoproceso')

@login_required(login_url='iniciarsesion')
def pedidoproceso(request):
    id_user = request.user.id
    contexto = {}
    contexto['pedidos'] = Pedido.objects.filter(id_usuario=id_user, st_pedido='PROCESO')
    contexto['pedidodetalles'] = Pedidodetalle.objects.filter(pedido__id_usuario=id_user, pedido__st_pedido='PROCESO')
    contexto['Qitems'] = get_Qitems(id_user)
    return render(request, 'pedidoproceso.html', contexto)

def get_Qitems(id_usuario):
    QItems = Pedidodetalle.objects.filter(pedido__id_usuario=id_usuario, pedido__st_pedido='PROCESO').count()
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
    pedidoitem = Pedidodetalle.objects.filter(pedido__id_pedido=pedido[0].id_pedido, producto=id)

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

