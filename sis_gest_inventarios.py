from abc import ABC, abstractmethod

class Producto(ABC): # Clase abstracta que define la estructura base de un producto

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @abstractmethod
    def mostrar_info(self): # Método abstracto que debe ser implementado por las subclases
        pass

class Electronico(Producto): # Subclases de producto
  
    def __init__(self, nombre, precio, stock, garantia):
        super().__init__(nombre, precio, stock)
        self.garantia = garantia

    def mostrar_info(self): # Muestra la informacion del producto
        return f"Electrónico: {self.nombre}, Precio: ${self.precio}, Stock: {self.stock}, Garantía: {self.garantia} meses"

class Alimento(Producto):

    def __init__(self, nombre, precio, stock, caducidad):
        super().__init__(nombre, precio, stock)
        self.caducidad = caducidad

    def mostrar_info(self):
        return f"Alimento: {self.nombre}, Precio: ${self.precio}, Stock: {self.stock}, Caducidad: {self.caducidad}"

class Ropa(Producto):

    def __init__(self, nombre, precio, stock, talla):
        super().__init__(nombre, precio, stock)
        self.talla = talla

    def mostrar_info(self):
        return f"Ropa: {self.nombre}, Precio: ${self.precio}, Stock: {self.stock}, Talla: {self.talla}"

class Inventario: # Manejo del inventario
                  # Esta clase maneja la gestion del mismo
    def __init__(self):
        self.productos = []  # Lista que almacena productos

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"    Producto '{producto.nombre}' agregado al inventario.")

    def listar_productos(self): 
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            print("\n - Inventario - :")
            for producto in self.productos:
                print(producto.mostrar_info())

def ingresar_producto(): # Permite capturar los datos del usuario
    # Retorna Producto (objeto) si la entrada es válida, None en caso contrario
    print("\n - Agregar un producto al inventario - ")
    print("1. Electrónico\n2. Alimento\n3. Ropa")
    tipo = input("Seleccione el tipo de producto (1/2/3): ")

    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock inicial: "))

    if tipo == "1":
        garantia = int(input("Garantía (en meses): "))
        return Electronico(nombre, precio, stock, garantia)
    elif tipo == "2":
        caducidad = input("Fecha de caducidad (DD/MM/YY): ")
        return Alimento(nombre, precio, stock, caducidad)
    elif tipo == "3":
        talla = input("Talla: ")
        return Ropa(nombre, precio, stock, talla)
    else:
        print("Opción inválida. No se agregó el producto.")
        return None

def main(): # Ejecuta el menu interactivo del sistema

    inventario = Inventario()

    while True:
        print("\n - Menú de Inventario - ")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto = ingresar_producto()
            if producto:
                inventario.agregar_producto(producto)
        elif opcion == "2":
            inventario.listar_productos()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
    
