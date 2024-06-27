from django.shortcuts import render
from .models import Producto


def index (request):
    context={}
    return render(request, 'tienda/index.html', context)


def listar_productos(request):
    productos = Producto.objects.all()  # Obtén todos los productos desde la base de datos
    return render(request, 'index.html', {'productos': productos})