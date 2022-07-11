from django.urls import path
from app_proyecto.views import clienteForm, vendedorForm, productoForm, mostrar_clientes, mostrar_inicio, mostrar_vendedores, mostrar_productos

urlpatterns = [
    path('home/', mostrar_inicio),
    path('clientes/', clienteForm),
    path('lista-clientes/', mostrar_clientes),
    path('vendedor/', vendedorForm),
    path('lista-vendedores/', mostrar_vendedores),
    path('productos/', productoForm),
    path('lista-productos/', mostrar_productos)
]