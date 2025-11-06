import json
ej1 = "dic_ej1.json"
ej2 = "dic_ej2.json"
ej3 = "dic_ej3.json"
ej4 = "dic_ej4.json"
ej5 = "dic_ej5.json"
ej6 = "dic_ej6.json"
ej7 = "dic_ej7.json"
ej8 = "dic_ej8.json"
ej9 = "dic_ej9.json"

def ejercicio1():
    informacion_personal = {
        "nombre": "Démian",
        "edad": "16",
        "Ciudad": "C.A.B.A",
        "Profesión": "Virgo momo"
    }
    for clave in informacion_personal:
        print(clave)
    with open(ej1, 'w', encoding='utf-8') as archivo:
        json.dump(informacion_personal, archivo, indent=4, ensure_ascii=False)
    print(f"¡Archivo '{ej1}' creado con éxito!")
ejercicio1()

def ejercicio2():
    informacion_personal = {
        "Nombre": "Démian",
        "Edad": "16",
        "Ciudad": "C.A.B.A",
        "Profesión": "Virgo momo"
    }
    informacion_personal["Ciudad"] = "Chechonlandia"
    informacion_personal["Profesión"] = "Chechista"
    informacion_personal["Teléfono"] = "11-2534-2426"
    informacion_personal["Email"] = "chechon.chechea@gmail.com"
    for clave, valor in informacion_personal.items():
        print(f"{clave}:{valor}")
    with open(ej2, 'w', encoding='utf-8') as archivo:
        json.dump(informacion_personal, archivo, indent=4, ensure_ascii=False)
    print(f"¡Archivo '{ej2}' creado con éxito!")
ejercicio2()

def ejercicio3():
    Calificaciones_Juanespechevereche = {
        "Matemáticas" : 8.5,
        "Lengua" : 11,
        "Educación Física" : 10,
        "Laboratorio" : 10
    }
    print(Calificaciones_Juanespechevereche["Lengua"])
    with open(ej3, 'w', encoding='utf-8') as archivo:
        json.dump(Calificaciones_Juanespechevereche, archivo, indent=4, ensure_ascii=False)
    print(f"¡Archivo '{ej3}' creado con éxito!")
ejercicio3()
def ejercicio4():
    promedio = 0
    Calificaciones_Juanespechevereche = {
        "Matemáticas": 8.5,
        "Lengua": 11,
        "Educación Física": 10,
        "Laboratorio": 10
    }
    for valor in Calificaciones_Juanespechevereche.values():
        promedio = promedio + valor
    promedio = promedio / 4
    print(promedio)
    with open(ej4, 'w', encoding='utf-8') as archivo:
        json.dump(Calificaciones_Juanespechevereche, archivo, indent=4, ensure_ascii=False)
    print(f"¡Archivo '{ej4}' creado con éxito!")
ejercicio4()
def ejercicio5():
    Paises_Capitales = {
        "México" : "Ciudad de México",
        "España" : "Madrid",
        "Argentina" : "Buenos Aires",
        "Francia" : "París",
        "Japón" : "Tokio",
        "Canadá" : "Ottawa",
        "Australia" : "Canberra",
        "Egipto" : "El Cairo",
        "India" : "Nueva Delhi",
        "Brasil" : "Brasilia"
    }
    Elige = input("Elige un País para ver su Capital: ")
    print(Paises_Capitales.get(Elige), "(Dato incorrecto o El país no está en la Lista)")
    with open(ej5, 'w', encoding='utf-8') as archivo:
        json.dump(Paises_Capitales, archivo, indent=4, ensure_ascii=False)
    print(f"¡Archivo '{ej5}' creado con éxito!")
ejercicio5()
def ejercicio6():
    Carrito = 0
    Items_Tienda = {
        "manzana": 3.50,
        "leche": 1.20,
        "pan": 2.00,
        "huevos": 2.50,
        "arroz": 1.00,
        "cafe": 4.00,
        "queso": 5.00,
        "tomates": 2.30,
        "pollo": 7.00,
        "azucar": 1.50
    }
    seguimos = True
    while seguimos:
            print("""|||||||||||||||Skibidi Market|||||||||||||||
                  PRODUCTOS
                  Manzana: 3.50
                  Leche: 1.20
                  Pan: 2.00
                  Huevos": 2.50
                  Arroz": 1.00
                  Cafe": 4.00
                  Queso": 5.00
                  Tomates": 2.30
                  Pollo": 7.00
                  Azucar": 1.50""")
            Producto = str(input("Elige el Producto que quieras llevar(Escriba salir para Salir): ")).lower()
            if Producto == "salir":
                break
            Cantidad = int(input("Elige la cantidad que vas a llevar: "))
            Carrito += Items_Tienda[Producto] * Cantidad
            print("Total: ",Carrito)
    with open(ej6, 'w', encoding='utf-8') as archivo:
        json.dump(Items_Tienda, archivo, indent=4, ensure_ascii=False)
    print(f"¡Archivo '{ej6}' creado con éxito!")
ejercicio6()
def ejercicio7():
    info_personal = {
        "Nombre": "Démian",
        "Edad": 16,
        "Ciudad": "Chechonlandia",
        "Profesión": "Chechista",
        "Teléfono": "11-2534-2426",
        "Email": "chechon.chechea@gmail.com"
    }
    del info_personal["Teléfono"]
    print(info_personal)
    with open(ej7, 'w', encoding='utf-8') as archivo:
        json.dump(info_personal, archivo, indent=4, ensure_ascii=False)
    print(f"¡Archivo '{ej7}' creado con éxito!")
ejercicio7()
def ejercicio8():
    dic1 = {
        "perro" : "animal",
        "gato" : "animal",
        "uno": 1,
        "dos": 2
    }
    esta = input("Ingrese la clave a buscar: ")
    if esta in dic1:
        print(dic1.get(esta), "True")
    else:
        print(dic1.get(esta), "False")
    with open(ej8, 'w', encoding='utf-8') as archivo:
        json.dump(dic1, archivo, indent=4, ensure_ascii=False)
    print(f"¡Archivo '{ej8}' creado con éxito!")
ejercicio8()
def ejercicio9():
    dic1 = {
        "nig" : 1,
        "ga" : 2
    }
    dic2 = {
        "nig" : 2,
        "ger" : 3
    }
    dic1.update(dic2)
    print(dic1)
    with open(ej1, 'w', encoding='utf-8') as archivo:
        json.dump(dic1, archivo, indent=4, ensure_ascii=False)
    print(f"¡Archivo '{ej1}' creado con éxito!")
ejercicio9()

