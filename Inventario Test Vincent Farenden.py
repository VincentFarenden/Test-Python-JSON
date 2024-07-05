import json
import os

# Código creado por Vincent Farenden
# Nombre del archivo para almacenar los datos
nombre_archivo = "inventario_archivos.json"

def cargar_inventario():
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as file:
            return json.load(file)
    return {}

def guardar_inventario(inventario):
    with open(nombre_archivo, 'w') as file:
        json.dump(inventario, file, indent=4)

def registrar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    
    inventario[nombre] = {"precio": precio, "cantidad": cantidad}
    print(f"Producto '{nombre}' registrado con éxito.")

def actualizar_inventario(inventario):
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    if nombre in inventario:
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        inventario[nombre]["cantidad"] = nueva_cantidad
        print(f"Cantidad de '{nombre}' actualizada a {nueva_cantidad}.")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")

def mostrar_inventario(inventario):
    if inventario:
        print("\nInventario actual:")
        for producto, detalles in inventario.items():
            print(f"{producto}: Precio: ${detalles['precio']:.2f}, Cantidad: {detalles['cantidad']}")
    else:
        print("El inventario está vacío.")

def menu():
    inventario = cargar_inventario()
    
    while True:
        print("\n--- Menú de Control de Inventario ---")
        print("1. Registre un producto")
        print("2. Actualice el inventario")
        print("3. Ver inventario")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_producto(inventario)
        elif opcion == "2":
            actualizar_inventario(inventario)
        elif opcion == "3":
            mostrar_inventario(inventario)
        elif opcion == "4":
            guardar_inventario(inventario)
            print("¡Gracias por usar el programa. :)!")
            break
        else:
            print("Opción no válida. Por favor intente de nuevo.")

if __name__ == "__main__":
    menu()