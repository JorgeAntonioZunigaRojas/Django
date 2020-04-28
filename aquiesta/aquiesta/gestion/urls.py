
from django.urls import path
from gestion import views

urlpatterns = [
    path('' , views.inicio.as_view(), name = 'inicio'),
    path('buscar/' , views.buscarProducto.as_view(), name = 'buscar'),
    path('producto/<int:id>' , views.get_producto, name = 'producto'),
    path('iniciarsesion/' , views.iniciarsesion, name = 'iniciarsesion'),
    path('cerrarsesion/' , views.cerrarsesion, name = 'cerrarsesion'),
    path('registarusuario/' , views.registarusuario, name = 'registarusuario'),
    path('agregarproducto/<int:id>' , views.agregarproducto, name = 'agregarproducto'),
    path('pedidoproceso/' , views.pedidoproceso, name = 'pedidoproceso'),
    path('confirmarcompra/<int:id>' , views.confirmarcompra, name = 'confirmarcompra'),
    path('iniciarsesionempresa/', views.iniciarsesionempresa, name = 'iniciarsesionempresa'),
    path('sisinicio/', views.sisInicio, name = 'sisinicio'),
    path('siscategoria/', views.sisCategoria, name = 'siscategoria'),
    path('siscerrarsesion/', views.sisCerrarSesion, name = 'siscerrarsesion'),
    path('siscategoriacrear/', views.sisCategoriaCrear.as_view(),name='siscategoriacrear'),
    
]

