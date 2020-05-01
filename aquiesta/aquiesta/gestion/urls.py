
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
    path('confirmarcompra/<int:id>' , views.confirmarcompra, name = 'confirmarcompra'),
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
    
]
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)


"""
from django.urls import path, include
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gallery/', include(('gallery.urls','gallery'))),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
"""




    
    



