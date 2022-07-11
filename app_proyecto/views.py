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
            return render(request, "app_proyecto/base.html")
    
    else:
        formcli = ClienteFormulario()
        return render(request, "app_proyecto/clientes.html", {'formcli':formcli})


def mostrar_clientes(request):
    listado = {'clientes':Cliente.objects.all()}
    return render(request, "app_proyecto/lista_clientes.html", listado)


def vendedorForm(request):
    if request.method == "POST":
        formven = VendedorFormulario(request.POST)
        print(formven)

        if formven.is_valid():
            datos = formven.cleaned_data
            vendedor1 = Vendedor(nombre=datos['nombre'], apellido=datos['apellido'], mail=datos['mail'], antiguedad=datos['antiguedad'])
            vendedor1.save()
            return render(request, "app_proyecto/base.html")
    
    else:
        formven = VendedorFormulario()
        return render(request, "app_proyecto/base.html", {'formven':formven})

def mostrar_vendedores(request):
    listado = {'vendedores':Vendedor.objects.all()}
    return render(request, "app_proyecto/lista_vendedores.html", listado)



def productoForm(request):
    if request.method == "POST":
        formprodu = ProductosFormulario(request.POST)
        print(formprodu)

        if formprodu.is_valid():
            datos = formprodu.cleaned_data
            producto1 = Productos(producto=datos['producto'], stock=datos['stock'])
            producto1.save()
            return render(request, "app_proyecto/base.html")
    
    else:
        formprodu = ProductosFormulario()
        return render(request, "app_proyecto/productos.html", {'formprodu':formprodu})


def mostrar_productos(request):
    listado = {'productos':Productos.objects.all()}
    return render(request, "app_proyecto/lista_productos.html", listado)



def buscar(request):
    if request.GET:
        #respuesta = f"Estoy buscando el item: {request.GET['producto']}"
        produ = request.GET['producto']
        filtro = Productos.objects.filter(producto__icontains=produ)

        return render(request,"app_proyecto/busquedaProducto.html", {"productos":filtro, "producto":produ})
    else:
        respuesta = "No hay datos con esa descripción"

    return render (request, "app_proyecto/busquedaProducto.html",{"respuesta":respuesta})