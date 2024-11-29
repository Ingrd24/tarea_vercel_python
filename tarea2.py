productos = []

def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    precio = input("Introduce el precio del producto: ")
    cantidad = input("Introduce la cantidad del producto: ")
    producto = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    productos.append(producto)
    print(f"Producto {nombre} añadido con éxito.\n")
    

def ver_productos():
    if productos:
        print("Lista de productos:")
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print("No hay productos en el inventario.\n")


def actualizar_producto():
    nombre = input("Introduce el nombre del producto que deseas actualizar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            print("1: Actualizar nombre")
            print("2: Actualizar precio")
            print("3: Actualizar cantidad")
            opcion = input("Selecciona qué deseas actualizar: ")

            if opcion == '1':
                nuevo_nombre = input("Introduce el nuevo nombre: ")
                producto['nombre'] = nuevo_nombre
            elif opcion == '2':
                nuevo_precio = float(input("Introduce el nuevo precio: "))
                producto['precio'] = nuevo_precio
            elif opcion == '3':
                nueva_cantidad = int(input("Introduce la nueva cantidad: "))
                producto['cantidad'] = nueva_cantidad
            else:
                print("Opción no válida.")
            print(f"Producto {nombre} actualizado con éxito.\n")
            return
    print(f"Producto {nombre} no encontrado.\n")


def eliminar_producto():
    nombre = input("Introduce el nombre del producto que deseas eliminar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            productos.remove(producto)
            print(f"Producto {nombre} eliminado con éxito.\n")
            return
    print(f"Producto {nombre} no encontrado.\n")


def guardar_datos():
    with open("productos.txt", "a") as file:
        for producto in productos:
            file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados en productos.txt.\n")


def cargar_datos():
    try:
        with open("productos.txt", "r") as file:
            for linea in file:
                nombre, precio, cantidad = linea.strip().split(',')
                productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
        print("Datos cargados desde productos.txt.\n")
    except FileNotFoundError:
        print("Archivo productos.txt no encontrado.\n")


def menu():
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")
menu()