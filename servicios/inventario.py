import os
from modelos.producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        #guardar todo en un .txt
        self.archivo = archivo
        self.__productos = [] # Mi lista privada de productos
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        #Manejo de FileNotFoundError
        if not os.path.exists(self.archivo): return
        try:
            # Abro el archivo en modo lectura ('r') para traer los datos
            with open(self.archivo, 'r') as f:
                for linea in f:
                    parts = linea.strip().split(',')
                    if len(parts) == 4:
                        p = Producto(parts[0], parts[1], int(parts[2]), float(parts[3]))
                        self.__productos.append(p)
            print("✓ Inventario cargado correctamente.")
        except Exception as e:
            print(f"Error al cargar archivo: {e}")

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, 'w') as f:
                for p in self.__productos:
                    f.write(f"{p.id},{p.nombre},{p.cantidad},{p.precio}\n")
        except PermissionError:
            print("Error: Sin permisos para escribir.")

    def agregar_producto(self, producto):
        if any(p.id == str(producto.id) for p in self.__productos):
            return False, "Error: El ID ya existe."
        self.__productos.append(producto)
        self.guardar_en_archivo()
        return True, "Producto guardado exitosamente."

    def eliminar_producto(self, id_p):
        id_p = str(id_p)
        original_count = len(self.__productos)
        self.__productos = [p for p in self.__productos if str(p.id) != id_p]
        if len(self.__productos) < original_count:
            self.guardar_en_archivo()
            return True
        return False

    def actualizar_producto(self, id_p, cantidad, precio):
       # Busco el producto por ID y le cambio los valores que quiero 
        for p in self.__productos:
            if str(p.id) == str(id_p):
                p.cantidad = cantidad
                p.precio = precio
                self.guardar_en_archivo()
                return True
        return False

    def buscar_por_nombre(self, nombre):
        # Filtro la lista buscando coincidencias, no importa si es mayúscula o minúscula
        return [p for p in self.__productos if nombre.lower() in p.nombre.lower()]

    def listar_productos(self):
        return self.__productos