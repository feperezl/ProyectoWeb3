from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar-producto', views.agregarProducto, name='agregar-producto'),
    path('listar-producto', views.listarProducto, name='listar-producto'),
    path('modificar-producto/<id>', views.modificarProducto, name='modificar-producto'),    
    path('eliminar-producto/<id>', views.eliminarProducto, name='eliminar-producto'),

]
