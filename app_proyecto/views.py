from django.shortcuts import render

def mostrar_inicio(request):
    return render(request, "app_proyecto/base.html", {})

def mostrar_clientes(request):
    return render(request, "app_proyecto/clientes.html", {})



def mostrar_vendedores(request):
    return render(request, "app_proyecto/vendedores.html", {})

def mostrar_productos(request):
    return render(request, "app_proyecto/productos.html", {})