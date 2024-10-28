# Sistema de Compra de Ropa en Python

Este proyecto es un sistema de compra de ropa en Python que simula el proceso de selección de artículos de ropa y compra mediante un menú interactivo en la consola. Este sistema usa los principios de Programación Orientada a Objetos (POO), incluyendo **Encapsulamiento**, **Herencia**, **Polimorfismo** y **Abstracción**.

## Estructura del Sistema

El sistema está compuesto por varias clases que representan los elementos clave de la tienda de ropa, y un menú interactivo que permite al usuario ver los productos disponibles y simular compras. A continuación, se detallan las clases y cómo se integran los principios de POO.

### Clases

#### 1. Clase `Prenda`
Representa una prenda genérica de ropa en la tienda. Esta clase incluye atributos y métodos básicos que se extienden en clases derivadas.

- **Atributos**:
  - `nombre`: Nombre de la prenda.
  - `precio`: Precio unitario de la prenda.
  - `cantidad`: Cantidad de stock disponible de la prenda.

- **Métodos**:
  - `mostrar_info()`: Muestra la información de la prenda, incluyendo nombre, precio y cantidad en stock.

#### 2. Clase `RopaHombre` (Hereda de `Prenda`)
Esta clase representa una prenda específica para hombres y extiende la clase `Prenda` con un atributo adicional `talla`. La herencia permite reutilizar los atributos y métodos de `Prenda`.

- **Atributos**:
  - `talla`: Talla de la prenda.

- **Métodos**:
  - `mostrar_info()`: Muestra la información de la prenda de hombre, incluyendo la `talla`. Este método sobrescribe el método de `Prenda`, mostrando el concepto de **Polimorfismo**.

#### 3. Clase `RopaMujer` (Hereda de `Prenda`)
Representa una prenda específica para mujeres y también extiende `Prenda` con el atributo `talla`.

- **Atributos**:
  - `talla`: Talla de la prenda.

- **Métodos**:
  - `mostrar_info()`: Sobrescribe el método `mostrar_info` de `Prenda` para incluir el atributo `talla`.

#### 4. Clase `Inventario`
Encapsula la lógica de agregar y gestionar las prendas en el inventario, aplicando el concepto de **Abstracción**. Esta clase actúa como un "contenedor" para los objetos `Prenda`, facilitando su gestión sin exponer detalles internos al usuario.

- **Atributos**:
  - `prendas`: Una lista que contiene todas las instancias de `Prenda` en el inventario.

- **Métodos**:
  - `agregar_prenda(prenda)`: Añade una prenda al inventario.
  - `mostrar_inventario()`: Muestra todos los productos disponibles en el inventario.
  - `comprar_prenda(nombre, cantidad)`: Procesa la compra de una prenda específica por su nombre y cantidad, verificando el stock disponible.

### Principios de POO en el Sistema

- **Encapsulamiento**: Los atributos de cada clase (`nombre`, `precio`, `cantidad`, `talla`) están encapsulados en sus respectivas clases.
- **Herencia**: `RopaHombre` y `RopaMujer` heredan de `Prenda`, reutilizando atributos y métodos.
- **Polimorfismo**: `mostrar_info()` está definido en `Prenda` y sobrescrito en `RopaHombre` y `RopaMujer`, permitiendo diferentes comportamientos.
- **Abstracción**: `Inventario` maneja las operaciones relacionadas con el inventario sin exponer los detalles internos de cómo se almacenan las prendas.

## Funcionamiento

1. El sistema crea instancias de `Prenda`, `RopaHombre`, y `RopaMujer`.
2. Estas instancias se agregan al `Inventario`.
3. Un menú interactivo permite al usuario:
   - Ver el inventario.
   - Seleccionar una prenda por su nombre.
   - Especificar la cantidad a comprar.
4. El inventario actualiza la cantidad de stock según las compras y muestra el inventario actualizado tras cada transacción.

## Ejemplo de Ejecución

1. El usuario ve el menú de compra con los artículos disponibles.
2. Ingresa el nombre de la prenda que quiere comprar.
3. Ingresa la cantidad deseada.
4. El sistema muestra si la compra se realizó correctamente o si hay falta de stock.
5. El inventario actualizado se muestra automáticamente después de cada compra.

## Requisitos Previos

- Python 3.x debe estar instalado para ejecutar el script.

## Ejecución del Sistema

Para ejecutar el sistema, usa el siguiente comando:

```bash
python nombre_del_archivo.py
