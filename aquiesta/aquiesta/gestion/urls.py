
from django.urls import path
from gestion import views
from aquiesta.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('' , views.inicio.as_view(), name = 'inicio'),
    path('buscar/' , views.buscarProducto.as_view(), name = 'buscar'),
    path('producto/<int:id>' , views.get_producto, name = 'producto'),
    path('iniciarsesion/' , views.iniciarsesion, name = 'iniciarsesion'),
    path('cerrarsesion/' , views.cerrarsesion, name = 'cerrarsesion'),
    path('registarusuario/' , views.registarusuario, name = 'registarusuario'),
    path('agregarproducto/<int:id>' , views.agregarproducto, name = 'agregarproducto'),
    path('pedidoproceso/' , views.pedidoproceso, name = 'pedidoproceso'),
    path('iniciarsesionempresa/', views.iniciarsesionempresa, name = 'iniciarsesionempresa'),
    path('siscerrarsesion/', views.sisCerrarSesion, name = 'siscerrarsesion'),
    path('sisinicio/', views.sisInicio, name = 'sisinicio'),
    path('siscategoria/', views.sis_categoria_lista, name = 'siscategoria'),
    path('siscategoriacrear/', views.sis_categoria_crear,name='siscategoriacrear'),
    path('siscategoriaeditar/<int:id>', views.sis_categoria_editar,name='siscategoriaeditar'),
    path('siscategoriaeliminar/<int:id>', views.sis_categoria_eliminar,name='siscategoriaeliminar'),

    path('sisproductolista/', views.sis_producto_lista, name = 'sisproductolista'),
    path('sisproductoeliminar/<int:id>', views.sis_producto_eliminar,name='sisproductoeliminar'),
    path('sisproductocrear/', views.sis_producto_crear,name='sisproductocrear'),
    path('sisproductoeditar/<int:id>', views.sis_producto_editar,name='sisproductoeditar'),
    
    path('sisusuariomtto/', views.sis_usuario_mtto, name='sisusuariomtto'),
    path('sisusuarioeditar/<int:id>', views.sis_usuario_editar,name='sisusuarioeditar'),

    path('sisempresamtto/', views.sis_empresa_mtto, name='sisempresamtto'),
    path('sisempresaeditar/<int:id>', views.sis_empresa_editar,name='sisempresaeditar'),

    path('usuariomtto/', views.usuario_mtto,name='usuariomtto'),
    path('usuarioeditar/<int:id>', views.usuario_editar,name='usuarioeditar'),
    
    path('pedidocomprar/<int:id>', views.pedido_comprar,name='pedidocomprar'),
    path('pedidopagar/<int:id>', views.pedido_pagar,name='pedidopagar'),

    path('sispedidopendienteentregalista/', views.sis_pedido_pendiente_entrega_lista,name='sispedidopendienteentregalista'),
    path('sispedidopendienteentregamtto/<int:id_pedido>', views.sis_pedido_pendiente_entrega_mtto,name='sispedidopendienteentregamtto'),
    path('sispedidopendienteanular/<int:id_pedido>', views.sis_pedido_pendiente_anular,name='sispedidopendienteanular'),
    path('sispedidopendienteentregar/<int:id_pedido>', views.sis_pedido_pendiente_entregar,name='sispedidopendienteentregar'),
    path('sispedidotodos/', views.sis_pedido_todos,name='sispedidotodos'),
    path('sispedidomtto/<int:id_pedido>', views.sis_pedido_mtto,name='sispedidomtto'),
]
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)



    
    



