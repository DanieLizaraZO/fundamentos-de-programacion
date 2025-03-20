"""
5. Dadas dos listas paralelas, una con nombres de productos y otra con sus precios, encuentra el producto más caro y el más barato.

"""
listaProductos = ["Laptop","Iphone","Tablet","Cargador","Forro"]
listaPrecios = [5,80,70,50,20]

listaParalela = list(zip(listaPrecios,listaProductos))
print(listaParalela)

masCaro = max(listaParalela)
masBarato = min(listaParalela)
print(f"El producto más caro es {masCaro}")
print(f"El producto más barato es {masBarato}")