productos = [
    {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica"},
    {"nombre": "Mouse", "precio": 25, "categoria": "Electrónica"},
    {"nombre": "Teclado", "precio": 75, "categoria": "Electrónica"},
    {"nombre": "Silla de Oficina", "precio": 300, "categoria": "Muebles"}]

estudiantes = [
        {"nombre": "Ana", "edad": 21, "calificacion": 90},
        {"nombre": "Luis", "edad": 22, "calificacion": 95},
        {"nombre": "Marta", "edad": 20, "calificacion": 85}
    ]

libros = [
    {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez"},
    {"titulo": "Don Quijote", "autor": "Miguel de Cervantes"},
    {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón"}
]

def ejercicio1():
    for productos_lista in productos:
        print(productos_lista)

def ejercicio2():
    acum = 0
    for x in range(len(productos)):
        acum += productos[x]["precio"]
    print(acum)

def ejercicio3():
    producto_auricular = {"nombre": "Auriculares","precio": 1200,"categoria": "Electrónica"}
    productos.append(producto_auricular)
    for x in productos:
        print(x)

def ejercicio4():
    productos[2]["precio"] = 40
    for x in productos:
        print(x)

def ejercicio5():
    nota_max = 0
    estudiante = 0
    for nota in estudiantes:
        if nota["calificacion"] > nota_max:
            nota_max = nota["calificacion"]
            estudiante = nota
    print(f"El Estudiante con mayor nota es: {estudiante}")

def ejercicio6():
    nombres_estudiantes = []
    for nombres in range(len(estudiantes)):
        nombres_estudiantes.append(estudiantes[nombres]["nombre"])
    print(nombres_estudiantes)

def ejercicio7(): #borrar Don Quijote
    libro_eliminado = libros.pop(1)
    for x in libros:
        print(x)


def ejercicio7mitad(): #Añadir Don Quijote
    libro_eliminado = libros.pop(1)
    Don_Quijote = {"titulo": "Don Quijote", "autor": "Miguel de Cervantes"}
    libros.append(Don_Quijote)
    for x in libros:
        print(x)

def ejercicio8():
    for clave in range(len(libros)):
        libros[clave]["Disponible"] = "True"
    for y in libros:
        print(y)
