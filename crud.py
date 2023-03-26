import json
from parametros_conexion import collection


def buscar_productos(nombre=None):
    if nombre is not None:
        query = {"nombre": nombre}
        document = collection.find_one(query)
        print(document)
    else:
        documents = collection.find().sort("categoria")
        for document in documents:
            print(document)


def buscar_categoria_productos(categoria=None):
    if categoria is not None:
        query = {"categoria": categoria}
        document = list(collection.find(query))
        print(*document, sep="\n")
    else:
        documents = collection.find()
        for document in documents:
            print(document)


def agregar_productos(producto):
    result = collection.insert_one(producto)
    print(result.inserted_id)


def modificar_productos(nombre, json_indices_valores):
    query = {"nombre": nombre}
    nuevo_valor ={"$set": json_indices_valores}
    result = collection.update_one(query, nuevo_valor)
    print(result.modified_count)


def eliminar_productos(nombre=None):
    if nombre is not None:
        query = {"nombre": nombre}
        document = collection.delete_one(query)
        print("Producto Eliminado")
    else:
        print("No se ha eliminado ningún producto")