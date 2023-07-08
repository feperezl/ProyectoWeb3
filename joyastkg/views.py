from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Producto, Carrito, bolsaCompra
from joyastkg.models import Carrito, Producto, bolsaCompra
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


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    
    return render(request, 'registro.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(to='index')
    # agregar mensaje de logout logrado

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

def mostrarCarrito(request):
    if request.user.is_authenticated:
        try:
            carrito = Carrito.objects.get(usuario=request.user)
            articulos = bolsaCompra.objects.filter(carrito=carrito)
            total = 0
            for articulo in articulos:
                total += articulo.producto.precio * articulo.cantidad
        except Carrito.DoesNotExist:
            carrito = None
            articulos = None
            total = 0
    else:
        carrito = None
        articulos = None
        total = 0

    # eliminar el producto
    if request.method == 'POST':
        bolsa_id = request.POST.get('bolsa_id')
        bolsa = bolsaCompra.objects.get(id=bolsa_id)
        bolsa.delete()

    return render(request, 'joyastkg/carrito.html', {'carrito': carrito, 'articulos': articulos, 'total': total})


def agregarCarrito(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        cantidad = int(request.POST.get('cantidad'))

        # Obtener el producto y el carrito
        producto = Producto.objects.get(id=producto_id)
        carrito, _ = Carrito.objects.get_or_create(usuario=request.user)

        bolsa = bolsaCompra.objects.create(carrito=carrito, producto=producto, cantidad=cantidad)
        bolsa.save()

        return redirect('carrito')


