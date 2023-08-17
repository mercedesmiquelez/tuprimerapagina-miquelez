from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('comprador/', views.comprador, name='comprador'),
    path('vendedor/', views.vendedor, name='vendedor'),
    path('producto/', views.producto, name='producto'),
    path('buscar_producto/', views.buscarProductos, name='BuscarProductos'),    
]