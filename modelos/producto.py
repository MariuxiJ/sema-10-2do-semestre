# modelos/producto.py

class Producto:
    
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto  # Atributo privado
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters y Setters con decoradores (Encapsulamiento)
    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def cantidad(self):
        return self.__cantidad

    # Setter para cantidad con validación lógica de negocio
    @cantidad.setter
    def cantidad(self, valor):
        if valor >= 0:
            self.__cantidad = valor
        else:
            print("Error: La cantidad no puede ser negativa.")

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor > 0:
            self.__precio = valor

    # Método especial para representar el objeto como una cadena de texto
    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Stock: {self.__cantidad} | Precio: ${self.__precio:.2f}"