from django.urls import path
from app_proyecto.views import buscar, clienteForm, vendedorForm, productoForm, mostrar_clientes, mostrar_inicio, mostrar_vendedores, mostrar_productos

urlpatterns = [
    path('inicio/', mostrar_inicio, name = 'inicio'),
    path('ingresar-cliente/', clienteForm, name = 'ingresar-cliente'),
    path('lista-clientes/', mostrar_clientes, name = 'lista-clientes'),
    path('ingresar-vendedor/', vendedorForm, name= 'ingresar-vendedor'),
    path('lista-vendedores/', mostrar_vendedores, name = 'lista-vendedores'),
    path('ingresar-producto/', productoForm, name= 'ingresar-producto'),
    path('lista-productos/', mostrar_productos, name= 'lista-productos'),
    path('buscar/', buscar, name = 'busqueda_productos'),
]