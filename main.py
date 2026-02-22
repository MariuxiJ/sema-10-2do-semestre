from modelos.producto import Producto
from servicios.inventario import Inventario

def menu():
    # Esto sigue igual: instancio mi clase inventario que ya carga el archivo solo
    inv = Inventario()
    
    while True:
        # Puse el menú para abajo (vertical) porque así se ve más ordenado que en una sola línea
        print("\n========================================")
        print("   SISTEMA DE GESTIÓN DE INVENTARIO")
        print("========================================")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar stock y precio")
        print("4. Buscar producto por nombre")
        print("5. Listar inventario")
        print("6. Salir del sistema")
        print("----------------------------------------")
        
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            # 1. Pedimos el ID como texto primero
            id_input = input("ID: ")
            
            # 2. VALIDACIÓN: ¿Son solo números?
            if not id_input.isdigit():
                print("\n[!] ERROR: El ID debe ser solo números (ejemplo: 101).")
                continue # Esto hace que regrese al menú sin dañarse
            
            try:
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                
                # Aquí llamas a tu función de agregar
                # inv.agregar_producto(Producto(id_input, nombre, cantidad, precio))
                print("\n>>> Producto agregado con éxito.")
                
            except ValueError:
                # Esto atrapa el error si ponen letras en Cantidad o Precio
                print("\n[!] ERROR: Cantidad y Precio deben ser valores numéricos.")

        elif opcion == "2":
            i = input("ID del producto a borrar: ")
            # CAMBIO: Ahora si el ID no existe, le aviso al usuario en lugar de que no haga nada
            if inv.eliminar_producto(i): 
                print("\n[OK] Ya se borró del archivo .txt.")
            else: 
                print(f"\n[!] AVISO: Ese ID '{i}' no existe, revisa el ID.")

        elif opcion == "3":
            try:
                # Esto es igual a lo anterior pero actualizado para persistencia
                i = input("ID a modificar: ")
                c = int(input("Nueva Cantidad: ")); p = float(input("Nuevo Precio: "))
                if inv.actualizar_producto(i, c, p): 
                    print("\n[OK] Cambios guardados en el archivo.")
                else: 
                    print(f"\n[!] AVISO: No encontré el ID '{i}'.")
            except ValueError: 
                print("\n[!] AVISO: Error en los datos, coloca números.")

        elif opcion == "4":
            # La búsqueda se mantiene igualita: recorre la lista y compara nombres
            n = input("Nombre a buscar: ")
            resultados = inv.buscar_por_nombre(n)
            if resultados:
                print(f"\n--- Resultados para '{n}' ---")
                for p in resultados: print(p)
            else:
                # CAMBIO: Aviso si la búsqueda sale vacía
                print(f"\n[!] AVISO: No encontré productos con el nombre '{n}' agregar en añadir producto o revisar inventario y verificar .")

        elif opcion == "5":
            # Listar sigue igual, solo que ahora los trae directo del archivo
            lista = inv.listar_productos()
            if lista:
                print("\n--- INVENTARIO ACTUAL ---")
                print(f"{'ID':<10} | {'NOMBRE':<20} | {'STOCK':<10} | {'PRECIO':<10}")
                print("-" * 65)
                
                for p in lista: 
                    print(p)
                print("="*65)
            else:
                print("\n[!] AVISO: El inventario está vacío.")

        elif opcion == "6":
            # Salir normal, avisando que todo se guardó bien
            print("\nGuardando todo... ¡Que tengas un buen dia!")
            break
            
        else:
            # CAMBIO: Aquí capturo cualquier huevada que escriban mal en el menú (como el "PAPA" que puse antes)
            print(f"\n[!] AVISO: '{opcion}' no es una opción del 1 al 6. Solo puedes colocar las opciones en patalla.")

if __name__ == "__main__":
    menu()