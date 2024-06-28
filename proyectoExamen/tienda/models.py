from django.db import models

class Producto(models.Model):

    ARTICULO = 'articulo'
    MACETA = 'maceta'
    PLANTA = 'planta'
    TIPO_CHOICES = [
        (ARTICULO, 'Artículo'),
        (MACETA, 'Maceta'),
        (PLANTA, 'Planta'),
    ]

    nombre = models.CharField(max_length=100)
    precio_con_descuento = models.IntegerField()
    precio_normal = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default=ARTICULO)

    def __str__(self):
        return self.nombre
