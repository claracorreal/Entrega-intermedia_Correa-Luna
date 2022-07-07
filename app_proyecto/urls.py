from django.urls import path
from app_proyecto.views import mostrar_inicio, mostrar_clientes, mostrar_productos, mostrar_vendedores

urlpatterns = [
    path('home/', mostrar_inicio),
    path('clientes/', mostrar_clientes),
    path('vendedores/', mostrar_vendedores),
    path('productos/', mostrar_productos),
]