class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Uso los dos guiones bajos para el encapsulamiento
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio
    # Estos @property son para poder leer los atributos privados desde afuera 
    @property
    def id(self): return self.__id
    @property
    def nombre(self): return self.__nombre
    @property
    def cantidad(self): return self.__cantidad
    # Este setter es para que no me dejen poner stock negativo por error
    @cantidad.setter
    def cantidad(self, valor):
        if valor >= 0: self.__cantidad = valor
        else: print("Error: Cantidad no negativa.")

    @property
    def precio(self): return self.__precio
    
    @precio.setter
    def precio(self, valor):
        if valor > 0: self.__precio = valor

    def __str__(self):
        # Esto alinea los datos para que parezcan columnas de una tabla
        return f"{str(self.id):<10} | {self.nombre:<20} | {str(self.cantidad):<10} | ${self.precio:<10.2f}"