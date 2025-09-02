def ejercicio1():
   matriz1 = [[1, 5, 3, 5],
              [8, 5, 9, 2],
              [4, 5, 6, 7],
              [2, 9, 1, 4]]
   for x in matriz1:
       filas_suma = 0
       print(x)
       for num in x:
           filas_suma += num
       print(f"La suma de esta fila es: {filas_suma}")
   for x in range(len(matriz1)):
       columnas_suma = 0
       for y in range(len(matriz1[x])):
           columnas_suma += matriz1[y][x]
           print(matriz1[y][x])
       print(f"La suma de esta Columna es: {columnas_suma}")


def ejercicio2():
   matriz2 = [[1, 5, 3, 5],
              [8, 5, 9, 2],
              [4, 5, 6, 7],
              [2, 9, 1, 4]]
   matriz_traspuesta = [[],
                        [],
                        [],
                        []]
   for fila in matriz2:
       print("Matriz Normal: ",fila)
   for x in range(len(matriz2)):
       for y in range(len(matriz2[x])):
           matriz_traspuesta[x].append(matriz2[y][x])
       for matriz_traspuesta_final in matriz_traspuesta:
           print(matriz_traspuesta_final)


def ejercicio3():
    opc = int(input("Ingrese un Número de la Matriz a Verificar: "))
    contador = 0
    matriz3 =   [[1, 5, 3, 5],
                [8, 5, 9, 2],
                [4, 5, 6, 7]]
    for fila in matriz3:
        print(fila)
        for numero in fila:
            if numero == opc:
                contador += 1
        print(f"El Número aparece {contador} veces")

def ejercicio4():
    promedio = 0
    matriz4x4 = [[1, 5, 3, 5],
                [8, 5, 9, 2],
                [4, 5, 6, 7],
                [2, 9, 1, 4]]
    matriz4x4_auxiliar = []
    for fila in matriz4x4:
        print(fila)
        for elemento in fila:
            promedio += elemento
    promedio = promedio/16
    for fila in matriz4x4:
        lista_auxiliar = []
        for elemento in fila:
            if elemento < promedio:
                lista_auxiliar.append(promedio)
            else:
                lista_auxiliar.append(elemento)
        matriz4x4_auxiliar.append((lista_auxiliar))
    for x in matriz4x4_auxiliar:
        print(x)