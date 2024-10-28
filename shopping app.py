class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre  
        self.precio = precio  
        self.cantidad = cantidad  
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Stock: {self.cantidad}")


class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad) 
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")


class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")


class Inventario:
    def __init__(self):
        self.prendas = [] 

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda) 

    def mostrar_inventario(self):
        print("\nInventario:")
        for prenda in self.prendas:
            prenda.mostrar_info()
        print("\n")

    def comprar_prenda(self, nombre, cantidad):
        for prenda in self.prendas:
            if prenda.nombre == nombre:
                if prenda.cantidad >= cantidad:
                    prenda.cantidad -= cantidad
                    print(f"\nCompra realizada: {cantidad} unidades de {nombre}.")
                    return
                else:
                    print(f"\nNo hay suficiente stock para {nombre}. Disponible: {prenda.cantidad}")
                    return
        print(f"\nLa prenda {nombre} no se encuentra en el inventario.")

camisa = RopaHombre("Camisa de Hombre", 25.00, 50, "M")
falda = RopaMujer("Falda de Mujer", 28.00, 15, "S")
inventario = Inventario()
inventario.agregar_prenda(camisa)
inventario.agregar_prenda(falda)

while True:
    print("\n--- Menú de Compras ---")
    inventario.mostrar_inventario()
    
    nombre_prenda = input("Ingrese el nombre de la prenda que desea comprar (o 'salir' para finalizar): ")
    if nombre_prenda.lower() == 'salir':
        break
    
    cantidad = int(input(f"Ingrese la cantidad de '{nombre_prenda}' que desea comprar: "))
    inventario.comprar_prenda(nombre_prenda, cantidad)
    
    inventario.mostrar_inventario()
