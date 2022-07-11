from django.urls import path
from app_proyecto.views import buscar, clienteForm, vendedorForm, productoForm, mostrar_clientes, mostrar_inicio, mostrar_vendedores, mostrar_productos

urlpatterns = [
    path('inicio/', mostrar_inicio),
    path('ingresar-cliente/', clienteForm),
    path('lista-clientes/', mostrar_clientes),
    path('ingresar-vendedor/', vendedorForm),
    path('lista-vendedores/', mostrar_vendedores),
    path('ingresar-producto/', productoForm),
    path('lista-productos/', mostrar_productos),
    path('buscar/', buscar),
]