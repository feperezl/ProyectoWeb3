from django import forms 
from .models import Producto
from joyastkg.models import bolsaCompra, Carrito, Producto



class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
