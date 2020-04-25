
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
]

    