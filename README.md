# SistemaGestionInventarios
Documentación
  Este sistema permite gestionar un inventario de productos utilizando polimorfismo y clases abstractas en Python. Soporta tres tipos de productos: Electrónicos, Alimentos y Ropa, cada uno con características específicas. 
  Características 
    •	Uso de clases abstractas para definir la estructura base de los productos. 
    •	Implementación de polimorfismo para manejar diferentes productos de manera uniforme. 
    •	Un menú interactivo para que el usuario pueda gestionar el inventario. 
    •	Métodos para agregar y listar productos.
  Estructura
    ‘Producto’ (Clase abstracta):
      •	Define los atributos y métodos comunes de los productos.
    Subclases de ‘Producto’:
      •	‘Electronico’: Agrega el atributo garantía.
      •	‘Alimento’: Agrega el atributo caducidad.
      •	‘Ropa’: Agrega el atributo talla.
    Clase ‘Inventario’:
      •	agregar_producto(producto): Añade un producto al inventario.
      •	listar_productos(): Muestra todos los productos en el inventario.
    Interfaz del usuario:
      •	ingresar_producto(): Solicita datos y crea productos dinámicamente.
      •	main(): Menú interactivo para la gestión del inventario.
