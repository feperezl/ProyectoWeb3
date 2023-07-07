from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tipo(models.Model):
    nombre = models.CharField(max_length=35)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    peso = models.CharField(max_length=4)
    imagen = models.ImageField(upload_to="productos", null=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto, through='bolsaCompra')

class bolsaCompra(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)