from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Ubigeo(models.Model):
    id_ubigeo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    class Meta:
        db_table = 'ubigeo'
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    tipo_doc_ident = models.CharField(max_length=1, blank=True, null=True)
    num_doc_ident = models.CharField(max_length=15, blank=True, null=True)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    ubigeo = models.ForeignKey(Ubigeo, models.DO_NOTHING, db_column='id_ubigeo', null=True)
    telefono = models.CharField(max_length=200, blank=True, null=True)
    imagen = models.CharField(max_length=200, blank=True, null=True)
    fecha_creacion=models.DateTimeField('Fecha de creación', auto_now=False, auto_now_add=True)
    fecha_edicion=models.DateTimeField('Fecha de edición', auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return self.nombre
    
class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    ruc = models.CharField(max_length=15, blank=True, null=True)
    rznsocial = models.CharField(max_length=200, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=200, blank=True, null=True)
    detalle = models.CharField(max_length=200, blank=True, null=True)
    ubigeo = models.ForeignKey('Ubigeo', models.DO_NOTHING, db_column='id_ubigeo', blank=True, null=True)
    imagen = models.CharField(max_length=200, blank=True, null=True)
    logo = models.CharField(max_length=200, blank=True, null=True)
    st_sgestion = models.CharField(max_length=200, default='EMITIDA')
    fecha_creacion=models.DateTimeField('Fecha de creación', auto_now=False, auto_now_add=True)
    fecha_edicion=models.DateTimeField('Fecha de edición', auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'empresa'

    def __str__(self):
        return self.rznsocial

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    fecha_creacion=models.DateTimeField('Fecha de creación', auto_now=False, auto_now_add=True)
    fecha_edicion=models.DateTimeField('Fecha de edición', auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return self.nombre

class Moneda(models.Model):
    id_moneda = models.CharField(primary_key=True, max_length=2)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    abreviatura = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'moneda'

    def __str__(self):
        return self.abreviatura

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)
    codigo = models.CharField(max_length=15, blank=True, null=True)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    moneda = models.ForeignKey(Moneda, models.DO_NOTHING, db_column='id_moneda', blank=True, null=True)
    precio = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    imagen = models.ImageField(upload_to = 'producto', default='static/imagen_no_disponible.png')
    fecha_creacion=models.DateTimeField('Fecha de creación', auto_now=False, auto_now_add=True)
    fecha_edicion=models.DateTimeField('Fecha de edición', auto_now=True, auto_now_add=False)
    
    class Meta:
        db_table = 'producto'

    def __str__(self):
        return self.nombre

class Productodetalle(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    clave = models.CharField(max_length=200, blank=True, null=True)
    valor = models.CharField(max_length=200, blank=True, null=True)
    fecha_creacion=models.DateTimeField('Fecha de creación', auto_now=False, auto_now_add=True)
    fecha_edicion=models.DateTimeField('Fecha de edición', auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'productodetalle'

    def __str__(self):
        return self.clave

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)
    serie = models.CharField(max_length=4, blank=True, null=True)
    numero = models.CharField(max_length=8, blank=True, null=True)
    fec_emision = models.DateTimeField(blank=True, null=True)
    id_usuario = models.IntegerField(null=True)
    tipo_doc_iden = models.CharField(max_length=1, blank=True, null=True)
    num_doc_iden = models.CharField(max_length=15, blank=True, null=True)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    ubigeo = models.ForeignKey('Ubigeo', models.DO_NOTHING, db_column='id_ubigeo', blank=True, null=True)
    telefono = models.CharField(max_length=200, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    entrega_domicilio = models.BooleanField(default=False)
    costo_entrega = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    st_pedido = models.CharField(max_length=200, blank=True, null=True)
    cancelado = models.BooleanField(default=False)
    fecha_creacion=models.DateTimeField('Fecha de creación', auto_now=False, auto_now_add=True)
    fecha_edicion=models.DateTimeField('Fecha de edición', auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'pedido'

    def __str__(self):
        return str(self.id_pedido)

class Pedidodetalle(models.Model):
    id_item = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='id_pedido', blank=False, null=False)
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    coproducto = models.CharField(max_length=15, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    fecha_creacion=models.DateTimeField('Fecha de creación', auto_now=False, auto_now_add=True)
    fecha_edicion=models.DateTimeField('Fecha de edición', auto_now=True, auto_now_add=False)
    
    class Meta:
        db_table = 'pedidodetalle'

    def __str__(self):
        return self.id_item 

