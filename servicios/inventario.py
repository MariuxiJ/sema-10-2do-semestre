# servicios/inventario.py
from modelos.producto import Producto

class Inventario:
    def __init__(self):
        # Estructura principal de almacenamiento: Lista privada
        self.__productos = []

    def agregar_producto(self, producto):
        # Validar que el ID no esté repetido
        if any(p.id == producto.id for p in self.__productos):
            return False, "Error: Ya existe un producto con ese ID."
        
        self.__productos.append(producto)
        return True, "Producto agregado con éxito."

    def eliminar_producto(self, id_producto):
        # Busca y elimina el objeto si el ID coincide
        for p in self.__productos:
            if p.id == id_producto:
                self.__productos.remove(p)
                return True
        return False

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Actualiza atributos usando setters del modelo Producto
        for p in self.__productos:
            if p.id == id_producto:
                if cantidad is not None: p.cantidad = cantidad
                if precio is not None: p.precio = precio
                return True
        return False

    def buscar_por_nombre(self, nombre):
        # Coincidencias parciales usando comprensión de listas
        return [p for p in self.__productos if nombre.lower() in p.nombre.lower()]

    def listar_productos(self):
        # Retorna la estructura principal para ser visualizada en la interfaz
        return self.__productos