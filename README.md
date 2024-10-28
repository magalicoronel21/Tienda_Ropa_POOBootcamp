# Sistema de Compra de Ropa
Este proyecto es un sistema de compras de ropa implementado en Python utilizando Programación Orientada a Objetos (POO). El sistema permite al usuario seleccionar diferentes tipos de ropa, agregar productos a un carrito y ver un resumen de su compra.
## Estructura del Proyecto
El proyecto incluye las siguientes clases:
### Clases Implementadas
1. **Producto**
   - Clase base que representa un producto general.
   - **Atributos**:
     - `nombre`: Nombre del producto.
     - `precio`: Precio del producto.
   - **Métodos**:
     - `mostrar_info()`: Muestra información del producto.
2. **Ropa**
   - Hereda de la clase `Producto`.
   - **Atributos adicionales**:
     - `talla`: Talla de la ropa.
   - **Métodos**:
     - `mostrar_info()`: Sobrescribe el método de la clase base para mostrar información específica de la ropa.
3. **Camisa**
   - Hereda de la clase `Ropa`.
   - Se utiliza para representar camisas.
4. **Pantalon**
   - Hereda de la clase `Ropa`.
   - Se utiliza para representar pantalones.
5. **Tienda**
   - Clase que maneja los productos disponibles y el carrito de compras.
   - **Atributos**:
     - `productos`: Lista de productos disponibles en la tienda.
     - `carrito`: Lista de productos seleccionados por el usuario.
   - **Métodos**:
     - `agregar_producto(producto)`: Agrega un producto a la tienda.
     - `mostrar_productos()`: Muestra la lista de productos disponibles.
     - `agregar_al_carrito(indice)`: Agrega un producto al carrito basado en su índice en la lista de productos.
     - `mostrar_resumen()`: Muestra un resumen de la compra y el total a pagar.
## Funcionamiento
1. **Agregar Productos**: Se crean instancias de `Camisa` y `Pantalon` y se agregan a la tienda.
2. **Mostrar Productos**: El programa muestra todos los productos disponibles para que el usuario seleccione.
3. **Interacción del Usuario**: El usuario puede seleccionar un producto escribiendo su número o salir escribiendo 'salir'.
4. **Resumen de Compra**: Al finalizar la selección, se muestra un resumen de los productos en el carrito y el total a pagar.
## Requisitos
- Python 3.x
## Ejecución
Para ejecutar el programa, sigue estos pasos:
1. Clona el repositorio o descarga los archivos.
2. Abre la terminal o consola de comandos.
3. Navega hasta el directorio donde se encuentra el archivo `sistema_compra.py`.
4. Ejecuta el siguiente comando:

   ```bash
   python sistema_compra.py

