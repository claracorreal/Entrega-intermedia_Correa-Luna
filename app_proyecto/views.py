from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from app_proyecto.models import Cliente, Vendedor, Productos
from app_proyecto.form import ClienteFormulario, VendedorFormulario, ProductosFormulario

def mostrar_inicio(request):
    return render(request, "app_proyecto/base.html", {})


def clienteForm(request):
    if request.method == "POST":
        formcli = ClienteFormulario(request.POST)
        print(formcli)

        if formcli.is_valid():
            datos = formcli.cleaned_data
            cliente1 = Cliente(empresa=datos['empresa'], mail=datos['mail'], fecha_compra=datos['fecha_compra'])
            cliente1.save()
            return render(request, "app_proyecto/clientes.html")
    
    else:
        formcli = ClienteFormulario()
        return render(request, "app_proyecto/clientes.html", {'formcli':formcli})


def mostrar_clientes(request):
    listado = {'clientes':Cliente.objects.all()}
    return render(request, "app_proyecto/lista_clientes.html", listado)


def mostrar_vendedores(request):
    return render(request, "app_proyecto/vendedores.html", {})

def mostrar_productos(request):
    return render(request, "app_proyecto/productos.html", {})