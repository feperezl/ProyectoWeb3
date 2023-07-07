from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Producto
from .forms import ProductoForm

# Create your views here.


def index(request):

    productos = Producto.objects.all()

    datos = {"productos": productos}

    return render(request, 'joyastkg/index.html', datos)

def disponible(request):
    
    productos = Producto.objects.all()
    datos = {"productos": productos}

    return render(request, 'joyastkg/productos.html', datos)

def contacto(request):
    
    productos = Producto.objects.all()
    datos = {"productos": productos}

    return render(request, 'joyastkg/contacto.html', datos)

def logout_view(request):
    logout(request)
    return redirect(to='index')

def agregarProducto(request):

    datos = {'form': ProductoForm()}

    if request.method == "POST":
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos["mensaje"] = "Guardado!"
        else:
            datos['form'] = formulario

    return render(request, 'joyastkg/producto/agregar.html',datos)

def listarProducto(request):
    productos = Producto.objects.all()
    datos = {'productos': productos}
    return render(request, 'joyastkg/producto/listar.html', datos)

@login_required
def modificarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    datos = {'form': ProductoForm(instance=producto)}
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos["mensaje"] = "Producto modificado!"
            return redirect(to="listar-producto")
    return render(request, 'joyastkg/producto/modificar.html', datos)


def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar-producto")