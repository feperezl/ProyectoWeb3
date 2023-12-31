from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos', views.disponible, name='productos'),
    path('contacto', views.contacto, name='contacto'),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('registro/', views.registro, name='registro'),
    path('carrito/', views.mostrarCarrito, name='carrito'),
    path('logout/', views.logout_view, name='logout'),
    path('agregar-producto', views.agregarProducto, name='agregar-producto'),
    path('listar-producto', views.listarProducto, name='listar-producto'),
    path('modificar-producto/<id>', views.modificarProducto, name='modificar-producto'),    
    path('eliminar-producto/<id>', views.eliminarProducto, name='eliminar-producto'),

]
