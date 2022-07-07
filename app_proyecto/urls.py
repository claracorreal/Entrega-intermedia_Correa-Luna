from django.urls import path
from app_proyecto.views import clienteForm, mostrar_clientes, mostrar_inicio, mostrar_productos, mostrar_vendedores

urlpatterns = [
    path('home/', mostrar_inicio),
    path('vendedores/', mostrar_vendedores),
    path('productos/', mostrar_productos),
    path('clientes/', clienteForm),
    path('lista-clientes/', mostrar_clientes),
]