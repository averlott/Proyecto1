#eju06-7

carritoCompra = {}

loop = "S"

nroArticulo = 1
precioTotalCarritoCompra = 0

while loop == "S":

    nombreProducto = input("Ingrese el nombre del producto que desea agregar a su carrito de compras: ")
    precioProducto = float(input("Ingrese el precio del producto que desea agregar a su carrito de compras: "))

    carritoCompra[nroArticulo] = {nombreProducto: precioProducto}

    nroArticulo += nroArticulo
    precioTotalCarritoCompra += precioProducto

    loop = input("¿Quiere seguir agregando productos a su carrito de compras? (S/N): ").upper()

#print(carritoCompra)

print('Lista de la compra:')

for articulo, producto in carritoCompra.items():
    for nombre,precio in producto.items():
        print(f'Artículo {articulo} -> nombre del producto: {nombre} precio del producto: {precio}')

print(f'Precio total del carrito de compras: {precioTotalCarritoCompra}')


