from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name = 'register'),
    path('login/', views.loginPage, name = 'login'),
    path('', views.home, name = 'home'),
    path('producto/', views.producto, name = 'producto'),
    path('logout/', views.logoutUser, name = 'logout'),
]

