class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre  # Atributo encapsulado
        self._precio = precio  # Atributo encapsulado
    
    # Getters y setters para el encapsulamiento
    def obtener_nombre(self):
        return self._nombre
    
    def obtener_precio(self):
        return self._precio
    
    # Método polimórfico
    def mostrar_info(self):
        raise NotImplementedError("Este método debe ser sobrescrito en las clases hijas")


class Ropa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla  # Atributo encapsulado

    def obtener_talla(self):
        return self._talla


class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela):
        super().__init__(nombre, precio, talla)
        self._tipo_tela = tipo_tela  # Atributo encapsulado
    
    def mostrar_info(self):
        print(f"Camisa: {self.obtener_nombre()}, Precio: ${self.obtener_precio()}, Talla: {self.obtener_talla()}, Tela: {self._tipo_tela}")


class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela):
        super().__init__(nombre, precio, talla)
        self._tipo_tela = tipo_tela  # Atributo encapsulado
    
    def mostrar_info(self):
        print(f"Pantalón: {self.obtener_nombre()}, Precio: ${self.obtener_precio()}, Talla: {self.obtener_talla()}, Tela: {self._tipo_tela}")


class Zapato(Ropa):
    def __init__(self, nombre, precio, talla, material):
        super().__init__(nombre, precio, talla)
        self._material = material  # Atributo encapsulado
    
    def mostrar_info(self):
        print(f"Zapato: {self.obtener_nombre()}, Precio: ${self.obtener_precio()}, Talla: {self.obtener_talla()}, Material: {self._material}")


class Tienda:
    def __init__(self):
        self._productos = []  # Lista de productos disponibles en la tienda
    
    def agregar_producto(self, producto):
        self._productos.append(producto)
    
    def mostrar_productos(self):
        print("Productos disponibles:")
        for idx, producto in enumerate(self._productos):
            print(f"{idx + 1}. ", end="")
            producto.mostrar_info()
    
    def obtener_producto(self, indice):
        if 0 <= indice < len(self._productos):
            return self._productos[indice]
        else:
            print("Índice de producto no válido.")
            return None


class Carrito:
    def __init__(self):
        self._items = []  # Lista de productos seleccionados
    
    def agregar_al_carrito(self, producto, cantidad):
        self._items.append((producto, cantidad))
    
    def mostrar_resumen(self):
        print("\nResumen de compra:")
        total = 0
        for producto, cantidad in self._items:
            subtotal = producto.obtener_precio() * cantidad
            print(f"{producto.obtener_nombre()} - Cantidad: {cantidad} - Subtotal: ${subtotal}")
            total += subtotal
        print(f"Total a pagar: ${total}")


# Interacción con el usuario
def iniciar_compra():
    tienda = Tienda()
    
    # Agregar productos a la tienda
    tienda.agregar_producto(Camisa("Camisa Casual", 20.00, "M", "Algodón"))
    tienda.agregar_producto(Pantalon("Pantalón Formal", 35.00, "L", "Poliéster"))
    tienda.agregar_producto(Zapato("Zapatos de Cuero", 50.00, "42", "Cuero"))
    
    carrito = Carrito()
    
    print("¡Bienvenido a la tienda de ropa!\n")
    
    while True:
        tienda.mostrar_productos()
        
        seleccion = input("Seleccione el número del producto que desea agregar al carrito (o 'q' para finalizar): ")
        
        if seleccion.lower() == 'q':
            break
        
        try:
            indice_producto = int(seleccion) - 1
            producto = tienda.obtener_producto(indice_producto)
            if producto:
                cantidad = int(input("Ingrese la cantidad deseada: "))
                carrito.agregar_al_carrito(producto, cantidad)
        except ValueError:
            print("Selección no válida. Por favor, intente de nuevo.")
    
    carrito.mostrar_resumen()
    print("Gracias por su compra.")


# Ejecución del programa
if __name__ == "__main__":
    iniciar_compra()
