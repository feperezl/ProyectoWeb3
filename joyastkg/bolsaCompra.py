from joyastkg.models import bolsaCompra, Carrito, Producto

carrito = Carrito.objects.get(id=1)  # Obtén el carrito existente de la base de datos
producto = Producto.objects.get(id=1)  # Obtén el producto existente de la base de datos
bolsa_compra = bolsaCompra(carrito=carrito, producto=producto, cantidad=1)
bolsa_compra.save()  # Guarda el objeto bolsaCompra en la base de datos
