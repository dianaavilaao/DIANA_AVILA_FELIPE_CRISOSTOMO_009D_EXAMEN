from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Cliente
from .forms import RegistroForm

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/index.html', {'productos': productos})

def producto_list_tipo(request, tipo_producto):
    productos = Producto.objects.filter(tipo=tipo_producto)
    return render(request, 'tienda/index.html', {'productos': productos, 'tipo_producto': tipo_producto})

def carrito(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/carrito.html', {'productos': productos})


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tienda/usuarios_list')  # Cambia esto a donde quieras redirigir después del registro
    else:
        form = RegistroForm()
    return render(request, 'tienda/registro.html', {'form': form})

def usuarios_list(request):
    clientes= Cliente.objects.all()
    return render(request, 'tienda/usuarios_list.html', {'clientes': clientes})

def eliminarUsuario(request, pk):
    try:
        cliente = Cliente.objects.get(username=pk)
        cliente.delete()
        mensaje = "Cliente eliminado"
    except Cliente.DoesNotExist:
        mensaje = "Cliente no encontrado"
    
    clientes = Cliente.objects.all()
    context = {'clientes': clientes, 'mensaje': mensaje}
    return redirect('usuarios_list')


#def eliminarUsuario(request, pk):
    context={}
    try:
        cliente=Cliente.objects.get(username=pk)

        cliente.delete()
        mensaje="Cliente eliminado"
        clientes=Cliente.objects.all()
        context={'alumnos' : clientes, 'mensaje':mensaje}
        return render(request, 'tienda/usuarios_list.html',context)
    except:
        mensaje="Cliente no encontrado"
        clientes=Cliente.objects.all()
        context={'alumnos' : clientes, 'mensaje':mensaje}
        return render(request, 'tienda/usuarios_list.html',context)