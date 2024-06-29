from django.urls import path
from . import views

urlpatterns = [
    path('index', views.producto_list, name='producto_list'),
    path('productos/<str:tipo_producto>/', views.producto_list_tipo, name='producto_list_tipo'),
    path('carrito', views.carrito, name='carrito'),
    path('registro', views.registro, name='registro'),
    path('usuarios_list', views.usuarios_list, name='registro'),
    path('eliminarUsuario/<str:pk>', views.eliminarUsuario, name="eliminarUsuario")
]
