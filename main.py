# main.py
from modelos.producto import Producto
from servicios.inventario import Inventario

def menu():
    mi_inventario = Inventario()
    # Se instancia el inventario FUERA del bucle para mantener los datos en memoria
    mi_inventario = Inventario()
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Listar inventario")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_p = int(input("ID único: "))
                nom = input("Nombre: ")
                cant = int(input("Cantidad: "))
                pre = float(input("Precio: "))
                # Creación del objeto Producto y envío al servicio
                nuevo = Producto(id_p, nom, cant, pre)
                exito, msg = mi_inventario.agregar_producto(nuevo)
                print(msg)
            except ValueError:
                print("Error: Entrada no válida. Use números para ID, cantidad y precio.")

        elif opcion == "2":
            try:
                # El 'try' protegerá el programa si el usuario escribe letras
                id_p = int(input("ID del producto a eliminar: "))
                if mi_inventario.eliminar_producto(id_p):
                    print("Producto eliminado.")
                else:
                    print("No se encontró un producto con ese ID.")
            except ValueError:
                
                print("Error: Debes ingresar el NÚMERO de ID, no el nombre.")

        elif opcion == "3":
            try:
                id_p = int(input("ID del producto a actualizar: "))
                nueva_cant = int(input("Nueva cantidad: "))
                nuevo_pre = float(input("Nuevo precio: "))
                if mi_inventario.actualizar_producto(id_p, nueva_cant, nuevo_pre):
                    print("Actualización exitosa.")
                else:
                    print(" Producto no encontrado.")
            except ValueError:
                print("Error: Para actualizar, todos los datos deben ser numéricos.")        

        
        elif opcion == "4":
             
            nom = input("Nombre a buscar: ")
            resultados = mi_inventario.buscar_por_nombre(nom)
            if resultados:
                for r in resultados: print(r)
            else:
                print("No hubo coincidencias.")

        elif opcion == "5":
            # Obtención de la lista y verificación de contenido
            lista = mi_inventario.listar_productos()
            if not lista:
                print("Inventario vacío.")
            for p in lista:
                print(p) #método __str__ de Producto

        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()