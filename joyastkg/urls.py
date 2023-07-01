from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos', views.disponible, name='productos'),
    path('admin/', admin.site.urls),
    path('acceso/', include('django.contrib.auth.urls')),
    path('agregar-producto', views.agregarProducto, name='agregar-producto'),
    path('listar-producto', views.listarProducto, name='listar-producto'),
    path('modificar-producto/<id>', views.modificarProducto, name='modificar-producto'),    
    path('eliminar-producto/<id>', views.eliminarProducto, name='eliminar-producto'),

]
