def busqueda_secuencial():
   valor_busqueda = int(input("Ingresá el valor a buscar: "))
   numeros = [34, 2, 17, 45, 23, 8, 12, 50, 27, 1, 33, 5, 49, 20, 14, 7, 38, 41, 19, 10, 29, 46, 3, 15, 9, 44, 6, 31, 22, 28, 4, 35, 18, 11, 39, 13, 24, 48, 16, 21, 30, 43, 26, 36, 47, 25, 40, 37, 32, 42]
   for i in range(len(numeros)):
       if numeros[i] == valor_busqueda:
           return i
   return -1


def busqueda_binaria():
    valor_busqueda = int(input("Ingresá el valor a buscar: "))
    numeros = [34, 2, 17, 45, 23, 8, 12, 50, 27, 1, 33, 5, 49, 20, 14, 7, 38, 41, 19, 10, 29, 46, 3, 15, 9, 44, 6, 31, 22, 28, 4, 35, 18, 11, 39, 13, 24, 48, 16, 21, 30, 43, 26, 36, 47, 25, 40, 37, 32, 42]
    valor = valor_busqueda
    izquierda = 0
    derecha = len(numeros) - 1
    n = len(numeros)
    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            if numeros[j] < numeros[minimo]:
                minimo = j
        numeros[i], numeros[minimo] = numeros[minimo], numeros[i]
    print(numeros)
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if numeros[medio] == valor:
               return medio
        elif numeros[medio] < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1


def busquedas():
   seguir = True
   while seguir:
       try:
           opc = int(input("""Hola Travieso, ¿Qué Búsqueda querés usar?
          1. Secuencial
          2. Binaria
          3. Volver al Menú
          : """))
           if opc == 1:
              indice = busqueda_secuencial()
              if indice != -1:
                  print("se encontró el numero en la posición:", indice)
              else:
                  print("no se encontró el numero")
           elif opc == 2:
               indice = busqueda_binaria()
               if indice != -1:
                   print(f"Se encontró el número en la posición: {indice}")
               else:
                   print("No se encontró el Número")
           elif opc == 3:
               seguir = False
       except ValueError:
           seguir = True




def ordenamiento_insercion():
   numeros = [34, 2, 17, 45, 23, 8, 12, 50, 27, 1, 33, 5, 49, 20, 14, 7, 38, 41, 19, 10, 29, 46, 3, 15, 9, 44, 6, 31, 22, 28, 4, 35, 18, 11, 39, 13, 24, 48, 16, 21, 30, 43, 26, 36, 47, 25, 40, 37, 32, 42]
   for i in range(1, len(numeros)):
       key = numeros[i]
       j = i - 1

       while j >= 0 and key < numeros[j]:
           numeros[j + 1] = numeros[j]
           j -= 1
       numeros[j + 1] = key
   print(numeros)
   return numeros



def ordenamiento_burbuja():
   numeros = [34, 2, 17, 45, 23, 8, 12, 50, 27, 1, 33, 5, 49, 20, 14, 7, 38, 41, 19, 10, 29, 46, 3, 15, 9, 44, 6, 31, 22, 28, 4, 35, 18, 11, 39, 13, 24, 48, 16, 21, 30, 43, 26, 36, 47, 25, 40, 37, 32, 42]
   n = len(numeros)
   for i in range(n - 1):
       Hay_Cambio = False
       for j in range(0, n - i - 1):
           if numeros[j] > numeros[j + 1]:
               numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
               Hay_Cambio = True
       if not Hay_Cambio:
           break
   print(numeros)
   return numeros


def ordenamiento_seleccion():
   numeros = [34, 2, 17, 45, 23, 8, 12, 50, 27, 1, 33, 5, 49, 20, 14, 7, 38, 41, 19, 10, 29, 46, 3, 15, 9, 44, 6, 31,22, 28, 4, 35, 18, 11, 39, 13, 24, 48, 16, 21, 30, 43, 26, 36, 47, 25, 40, 37, 32, 42]
   n = len(numeros)
   for i in range(n):
       minimo = i
       for j in range(i + 1, n):
           if numeros[j] < numeros[minimo]:
               minimo = j
       numeros[i], numeros[minimo] = numeros[minimo], numeros[i]
   print(numeros)
   return numeros


def menu():
   seguir = True
   while seguir:
       try:
           opc = int(input("""                       |||||||||Hola Travieso||||||||
                  |||¿Qué querés hacer con la lista?|||
                  |||1. Ordenamientos               |||
                  |||2. Búsquedas                   |||
                  |||3. Sybau💔                    |||
                  ||||||||||||||||||||||||||||||||||||
                  Elección: """))
           if opc == 1:
               print("Método de ordenamiento:")
               print("1) Inserción")
               print("2) Burbuja")
               print("3) Selección")
               metodo = int(input("Elige 1/2/3: "))
               if metodo == 1:
                   ordenamiento_insercion()
               elif metodo == 2:
                   ordenamiento_burbuja()
               else:
                   ordenamiento_seleccion()

           elif opc == 2:
               busquedas()
           elif opc == 3:
               break
       except ValueError:
           seguir = True
menu()
