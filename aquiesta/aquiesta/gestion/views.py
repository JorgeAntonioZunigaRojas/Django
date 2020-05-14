from django.shortcuts import render
# Create your views here.

from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView, CreateView, View, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator

from gestion.forms import CrearUsuarioForm, CategoriaForm, ProductoForm, UsuarioForm, EmpresaForm
from gestion.models import Moneda, Ubigeo
from gestion.models import Producto, Empresa, Productodetalle, Usuario, Pedido, Pedidodetalle, Categoria
from django.db.models import Q
from datetime import datetime
from decimal import Decimal

@login_required(login_url='iniciarsesionempresa')
def sis_pedido_mtto(request, id_pedido):
    contexto = get_contexto(request)
    contexto['pedido'] = Pedido.objects.get(id_pedido=id_pedido)
    contexto['detalle'] = Pedidodetalle.objects.filter(pedido__id_pedido=id_pedido)
    return render(request, 'sis_pedido_mtto.html', contexto)

@login_required(login_url='iniciarsesionempresa')
def sis_pedido_todos(request):
    pedidos = Pedido.objects.all().exclude(st_pedido='PROCESO')
    consulta = request.GET.get('buscar')
    if consulta:
        pedidos = pedidos.filter(Q(nombre__icontains = consulta) | Q(num_doc_iden__icontains = consulta) | Q(id_pedido__icontains = consulta))
    contexto = get_contexto(request)
    contexto['pedidos'] = pedidos
    return render(request, 'sis_pedido_todos.html', contexto)

@login_required(login_url='iniciarsesionempresa')
def sis_pedido_pendiente_entregar(request, id_pedido):
    pedido = Pedido.objects.get(id_pedido=id_pedido)
    contexto = get_contexto(request)
    contexto['pedido'] = pedido
    if request.method=='POST':
        pedido.st_pedido='ENTREGADO'
        pedido.save()
        return redirect('sispedidopendienteentregalista')
    return render(request, 'pedido_confirm_entrega.html', contexto)
    
@login_required(login_url='iniciarsesionempresa')
def sis_pedido_pendiente_anular(request, id_pedido):
    pedido = Pedido.objects.get(id_pedido=id_pedido)
    contexto = get_contexto(request)
    contexto['pedido'] = pedido
    if request.method=='POST':
        pedido.st_pedido='ANULADO'
        pedido.save()
        return redirect('sispedidopendienteentregalista')
    return render(request, 'pedido_confirm_delete.html', contexto)
    
@login_required(login_url='iniciarsesionempresa')
def sis_pedido_pendiente_entrega_mtto(request, id_pedido):
    contexto = get_contexto(request)
    contexto['pedido'] = Pedido.objects.get(id_pedido=id_pedido)
    contexto['detalle'] = Pedidodetalle.objects.filter(pedido__id_pedido=id_pedido)
    return render(request, 'sis_pedido_pendiente_entrega_mtto.html', contexto)

@login_required(login_url='iniciarsesionempresa')
def sis_pedido_pendiente_entrega_lista(request):
    pedidos = Pedido.objects.filter(st_pedido='COMPRADO')
    consulta = request.GET.get('buscar')
    if consulta:
        pedidos = pedidos.filter(Q(nombre__icontains = consulta) | Q(num_doc_iden__icontains = consulta) | Q(id_pedido__icontains = consulta))
    contexto = get_contexto(request)
    contexto['pedidos'] = pedidos
    return render(request, 'sis_pedido_pendiente_entrega_lista.html', contexto)

@login_required(login_url='iniciarsesionempresa')
def sis_empresa_editar(request, id):
    mensaje = ''
    error =[]
    empresa_form = []
    try:
        empresa = Empresa.objects.get(id_empresa=id)
        if request.method=='GET':
            empresa_form = EmpresaForm(instance=empresa)
        else:
            empresa_form = EmpresaForm(request.POST, request.FILES, instance=empresa)
            if empresa_form.is_valid():
                empresa_form.save()
                return redirect('sisempresamtto')
            else:
                mensaje = 'Datos NO validos'
    except ObjectDoesNotExist as e:
        error = e
    contexto = {
        'form': empresa_form,
        'empresa': empresa,
        'error': error,
        'mensaje': mensaje,
    }
    return render(request, 'sis_empresa_editar.html', contexto)

@login_required(login_url='iniciarsesionempresa')
def sis_empresa_mtto(request):
    contexto = get_contexto(request)
    empresa = Empresa.objects.get(usuario__id_usuario=request.user.id)
    contexto['form']= EmpresaForm(instance=empresa)
    contexto['empresa']= empresa
    return render(request,'sis_empresa_mtto.html', contexto)

@login_required(login_url='iniciarsesionempresa')
def sis_usuario_editar(request, id):
    error = []
    usuario_form = []
    mensaje = ''
    distritos = Ubigeo.objects.filter(id_ubigeo__contains='1401').exclude(id_ubigeo='140100')

    try:
        usuario = Usuario.objects.get(id_usuario=id)
        if request.method == 'GET':
            usuario_form = UsuarioForm(instance=usuario)
        else:
            usuario_form = UsuarioForm(request.POST, request.FILES, instance=usuario)
            if usuario_form.is_valid():
                usuario_form.save()
                return redirect('sisusuariomtto')
            else:
                mensaje = 'Datos incompletos...!!!'

    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'sis_usuario_editar.html', {'form':usuario_form, 'id_usuario': id, 'error': error, 'mensaje':mensaje, 'distritos':distritos, 'usuario':usuario})

@login_required(login_url='iniciarsesionempresa')
def sis_usuario_mtto(request):
    contexto = get_contexto(request)
    usuario = Usuario.objects.get(id_usuario=request.user.id)
    contexto['form']= UsuarioForm(instance=usuario)
    contexto['usuario']= usuario
    return render(request,'sis_usuario_mtto.html', contexto)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

@login_required(login_url='iniciarsesionempresa')
def sis_producto_editar(request, id):
    error = []
    producto_form = []
    try:
        producto = Producto.objects.get(id_producto=id)
        if request.method=='GET':
            producto_form = ProductoForm(instance=producto)
        else:
            producto_form = ProductoForm(request.POST, request.FILES, instance=producto)
            if producto_form.is_valid():
                producto_form.save()
                return redirect('sisproductolista')
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'sis_producto_editar.html', {'form': producto_form, 'id_producto': id, 'error': error})

@login_required(login_url='iniciarsesionempresa')
def sis_producto_crear(request):
    producto_form = ProductoForm()
    id_empresa = get_contexto(request)['id_empresa']
    categoria = Categoria.objects.filter(empresa__id_empresa=id_empresa)
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, request.FILES)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('sisproductolista')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'sisproductolista'}}">reload</a>""")
    return render(request,'sis_producto_crear.html', {'form':producto_form, 'categorias': categoria})

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
    print(request.GET)
    consulta = request.GET.get('buscar')
    contexto = get_contexto(request)
    id_empresa = contexto['id_empresa']

    productos = Producto.objects.filter(categoria__empresa__id_empresa=id_empresa)
    if consulta:
        productos = productos.filter(Q(nombre__icontains = consulta) | Q(codigo__icontains = consulta) | Q(categoria__nombre__icontains = consulta))

    productos = productos.values('id_producto', 'codigo', 'nombre', 'categoria__nombre', 'moneda__abreviatura', 'precio', 'imagen').order_by('-fecha_edicion','nombre')
    paginador = Paginator(productos, 16)
    page = request.GET.get('page')
    productos = paginador.get_page(page)
    contexto['productos'] = productos
    print(contexto)
    return render(request, 'sis_producto_lista.html', contexto)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

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
    consulta = request.GET.get('buscar')
    contexto = get_contexto(request)
    empresa = contexto['empresa']
    categorias = Categoria.objects.filter(empresa__id_empresa=empresa.id_empresa)
    if consulta:
        categorias = categorias.filter(nombre__icontains = consulta)
    categorias = categorias.order_by('-fecha_edicion')
    paginador = Paginator(categorias, 16)
    page = request.GET.get('page')
    categorias = paginador.get_page(page)
    contexto['categorias'] = categorias
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
    QPxDespachar = Pedido.objects.filter(empresa__id_empresa=empresa.id_empresa, st_pedido='COMPRADO').count()
    id_empresa = empresa.id_empresa
    contexto['empresa'] = empresa
    contexto['usuario'] = usuario
    contexto['id_empresa'] = id_empresa
    contexto['QPxDespachar'] = QPxDespachar
    return contexto

@login_required(login_url='iniciarsesionempresa')
def sisInicio(request):
    contexto = get_contexto(request)
    id_user = request.user.id
    empresa = contexto['empresa']
    id_empresa = empresa.id_empresa
    QPEntregados = Pedido.objects.filter(empresa__id_empresa=id_empresa, st_pedido='ENTREGADO').count()
    QPEmitidos = Pedido.objects.filter(empresa__id_empresa=id_empresa).exclude(st_pedido='PROCESO').count()
    QCategorias = Categoria.objects.filter(empresa__id_empresa=id_empresa).count()
    QProductos = Producto.objects.filter(categoria__empresa__id_empresa=id_empresa).count()
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
def pedido_pagar(request, id):
    pedido = Pedido.objects.get(id_pedido=id)
    pedido.st_pedido='COMPRADO'
    pedido.nombre = request.POST.get('nombre')
    pedido.tipo_doc_iden = request.POST.get('tipo_doc_ident')
    pedido.num_doc_iden = request.POST.get('num_doc_ident')
    pedido.telefono = request.POST.get('telefono')
    pedido.fec_emision = datetime.now()
    print(request.POST.get('tipo_doc_ident'))

    pedido.save()
    return pedido_comprar(request, id)

@login_required(login_url='iniciarsesion')
def pedido_comprar(request, id):
    context = {}
    context['Qitems'] = get_Qitems(request.user.id)
    context['form_usuario'] = UsuarioForm(instance=Usuario.objects.get(id_usuario=request.user.id))
    context['pedido'] = Pedido.objects.get(id_pedido=id)
    return render(request, 'pedido_comprar.html', context)

@login_required(login_url='iniciarsesion')
def pedidoproceso(request):
    id_user = request.user.id
    contexto = {}
    pedidodetalle = Pedidodetalle.objects.filter(pedido__id_usuario=id_user, pedido__st_pedido='PROCESO')
    contexto['pedidos'] = Pedido.objects.filter(id_usuario=id_user, st_pedido='PROCESO')
    contexto['pedidodetalles'] = pedidodetalle
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
    else:
        pedido = pedido[0]

    pedidoitem = Pedidodetalle.objects.filter(pedido__id_pedido=pedido.id_pedido, producto=id)

    if not pedidoitem:
        pedidoitem = Pedidodetalle.objects.create(
            pedido = pedido, 
            producto = producto, 
            coproducto = producto.codigo, 
            descripcion = producto.nombre, 
            cantidad = 1, 
            precio = producto.precio,
        )
        pedidodetalle = Pedidodetalle.objects.filter(pedido__id_pedido=pedido.id_pedido)
        subtotal = Decimal(0.00)
        for item in pedidodetalle:
            subtotal = subtotal + Decimal(item.cantidad*item.precio)
        pedido.subtotal = subtotal
        pedido.costo_entrega=0
        pedido.save()
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
                messages.success(request,'Usuario [' + user + '] su cuenta ha sido creada')
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


@login_required(login_url='iniciarsesionempresa')
def usuario_editar(request, id):
    error = []
    usuario_form = []
    mensaje = ''

    try:
        usuario = Usuario.objects.get(id_usuario=id)
        if request.method == 'GET':
            usuario_form = UsuarioForm(instance=usuario)
        else:
            usuario_form = UsuarioForm(request.POST, request.FILES, instance=usuario)
            if usuario_form.is_valid():
                usuario_form.save()
                return redirect('usuariomtto')
            else:
                mensaje = 'Datos incompletos...!!!'

    except ObjectDoesNotExist as e:
        error = e

    contexto={}
    contexto['form'] = usuario_form
    contexto['id_usuario'] = id
    contexto['error'] = error
    contexto['mensaje'] = mensaje
    contexto['usuario'] = usuario
    contexto['Qitems'] = get_Qitems(request.user.id)

    return render(request, 'usuario_editar.html', contexto)

@login_required(login_url='iniciarsesion')
def usuario_mtto(request):
    contexto={}
    usuario = Usuario.objects.get(id_usuario=request.user.id)
    contexto['Qitems'] = get_Qitems(request.user.id)
    contexto['form']= UsuarioForm(instance=usuario)
    contexto['usuario']= usuario
    return render(request,'usuario_mtto.html', contexto)

class buscarProducto(ListView):
    model = Producto
    template_name = 'principal.html'
    def get_queryset(self, ):
        p_buscar = self.request.GET.get('producto')
        return self.model.objects.filter(nombre__icontains=p_buscar)
    def get_context_data(self, request, **kwargs):
        contexto = {}
        contexto['productos'] = self.get_queryset()
        contexto['Qitems'] = get_Qitems(request.user.id)
        contexto['buscar'] = self.request.GET.get('producto')
        return contexto
    def get(self, request,*args,**kwargs):
        return render(request, self.template_name,self.get_context_data(request))

class inicio(ListView):
    model = Producto
    template_name = 'principal.html'
    def get_queryset(self, ):
        return self.model.objects.all().order_by('-fecha_creacion', 'nombre')[:12]
    def get_context_data(self, request, **kwargs):
        contexto = {}
        contexto['productos'] = self.get_queryset()
        contexto['Qitems'] = get_Qitems(request.user.id)
        return contexto
    def get(self, request,*args,**kwargs):
        return render(request, self.template_name,self.get_context_data(request))

