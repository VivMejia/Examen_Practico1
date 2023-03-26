from crud import *
from funciones_basicas import *

while True:
    print("*************************")
    print("         MENÚ            ")
    print("*************************")
    print("1. Ver todos los productos")
    print("2. Buscar producto por Categoria")
    print("3. Buscar producto por Nombre")
    print("4. Agregar Producto")
    print("5. Modificar Producto")
    print("6. Eliminar Producto")
    print("7. Salir de sistema")
    opcion = input("\nSeleccione una opción: \n")

    if opcion == "1":
        buscar_productos()
    elif opcion == "2":
        categoria = input("Ingrese el nombre de la categoria a buscar: ")
        buscar_categoria_productos(categoria)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto a buscar: ")
        buscar_productos(nombre)
    elif opcion == "4":
        producto = agregar_json_productos()
        agregar_productos(producto)
    elif opcion == "5":
        nombre = input("Ingrese el nombre del producto a modificar: ")
        producto = crear_json_actualizar_productos()
        modificar_productos(nombre, producto)
    elif opcion == "6":
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        eliminar_productos(nombre)
    elif opcion == "7":
        print("Saliendo del sistema")
        break
