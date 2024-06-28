from django.urls import path
from . import views

urlpatterns = [
    path('index', views.producto_list, name='producto_list'),
    path('productos/<str:tipo_producto>/', views.producto_list_tipo, name='producto_list_tipo')
]
