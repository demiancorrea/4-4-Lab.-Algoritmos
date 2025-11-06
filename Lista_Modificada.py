import json
lista_modificada = "Lista_Modificada.json"
productos = [
    {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica"},
    {"nombre": "Mouse", "precio": 25, "categoria": "Electrónica"},
    {"nombre": "Teclado", "precio": 75, "categoria": "Electrónica"},
    {"nombre": "Silla de Oficina", "precio": 300, "categoria": "Muebles"}]

def ejercicio3():
    producto_auricular = {"nombre": "Auriculares","precio": 1200,"categoria": "Electrónica"}
    productos.append(producto_auricular)
    for x in productos:
        print(x)
ejercicio3()
def ejercicio4():
    productos[2]["precio"] = 40
    for x in productos:
        print(x)
ejercicio4()

with open(lista_modificada, 'w', encoding='utf-8') as archivo:
   json.dump(productos, archivo, indent=4, ensure_ascii=False)
print(f"¡Archivo '{lista_modificada}' creado con éxito!")