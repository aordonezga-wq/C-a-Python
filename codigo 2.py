productosRegistrados = 0
productosConDescuento = 0
totalCompras = 0
totalPagado = 0
producto = input("Ingrese el nombre del producto (FIN para terminar): ")
while producto != "FIN":
    cantidad = input("Ingrese la cantidad: ")
    cantidadi= int(cantidad)
    precio = input("Ingrese el precio unitario: ")
    preciof = float(precio)
    productosRegistrados += 1
    totalproducto = cantidadi * preciof
    descuento = 0.0
    if totalproducto >= 100000:
        descuento = totalproducto * 0.10
        productosConDescuento += 1
    elif totalproducto >= 50000:
        descuento = totalproducto * 0.05
        productosConDescuento += 1
    valorFinal = totalproducto - descuento
    totalCompras += totalproducto
    totalproductos = str(totalproducto)
    totalPagado += valorFinal
    valorFinals = str(valorFinal)
    descuentos = str(descuento)
    print("\nProducto: "+ producto)
    print("Valor original: $"+ totalproductos)
    print("Descuento: $"+ descuentos)
    print("Valor a pagar: $"+ valorFinals)
    producto = input("\nIngrese el nombre del producto (FIN para terminar): ")
print("\n--- RESUMEN DE LA COMPRA ---")
productosRegistradoss = str(productosRegistrados)
print("Productos registrados: "+ productosRegistradoss)
productosConDescuentos = str(productosConDescuento)
print("Productos con descuento: "+ productosConDescuentos)
totalComprass = str(totalCompras)
print("Valor original de las compras: $"+ totalComprass)
totalPagados = str(totalPagado)
print("Valor final a pagar: $"+ totalPagados)