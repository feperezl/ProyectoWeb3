from django.db import models

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
