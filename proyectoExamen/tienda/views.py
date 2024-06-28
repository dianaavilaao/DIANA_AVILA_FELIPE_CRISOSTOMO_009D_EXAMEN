from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm



def index (request):
    context={}
    return render(request, 'tienda/index.html', context)


def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/index.html', {'productos': productos})

def producto_list_tipo(request, tipo_producto):
    productos = Producto.objects.filter(tipo=tipo_producto)
    return render(request, 'tienda/index.html', {'productos': productos, 'tipo_producto': tipo_producto})