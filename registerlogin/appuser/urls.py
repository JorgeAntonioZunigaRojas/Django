from django.urls import path
from appuser import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.principal, name = 'principal'),
    path('iniciarsesion/', views.iniciarsesion, name = 'iniciarsesion'),
    path('registrar/', views.registro, name = 'registrar'),
    path('cerrarsesion/', views.cerrarsesion, name = 'cerrarsesion'),
    path('producto/', views.producto, name = 'producto'),
    path('cliente/', views.cliente, name = 'cliente'),
]


