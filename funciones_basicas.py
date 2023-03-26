def agregar_json_productos():
    nombre = input("Nombre: ")
    precio = (input("Precio: "))
    categoria = input("Categoría: ")

    producto = {
        "nombre": nombre,
        "precio": precio,
        "categoria": categoria,

    }
    return producto


def crear_json_actualizar_productos():
    print("Menu de opciones ")
    print("1. Modificar todo el producto")
    print("2. Modificar solo una caracteristica del producto: ")
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        precio = input("Precio: ")
        categoria = input("Categoría: ")

        producto = {
            "nombre": nombre,
            "precio": precio,
            "categoria": categoria,

        }
        return producto
    elif opcion == "2":
        indice = input("Ingrese el valor del campo a modificar: ")
        valor = input("Ingrese el valor a modificar")
        producto = {indice:valor}
        return producto
