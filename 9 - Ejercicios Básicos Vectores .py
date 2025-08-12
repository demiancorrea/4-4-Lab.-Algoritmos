def ejercicio1():
    numeros_ingresados = 5
    listanumeros = []
    while numeros_ingresados != 0:
        try:
            numeros = int(input("Ingrese un Número: "))
            listanumeros.append(numeros)
            numeros_ingresados = numeros_ingresados - 1

            if numeros_ingresados == 0:
                for x in range(0, len(listanumeros)):
                    print(listanumeros[x])

        except ValueError:
            print("Valor Incorrecto, Inténtelo de Nuevo")

def ejercicio2():
    try:
        frutas = ["manzana","banana","fruta del dragon","mango celeste"]
        ingresarfruta = input("Ingrese la Fruta a Buscar: ")
        busqueda_fruta = frutas.index(ingresarfruta)
        print(f"La Fruta '{ingresarfruta}' Está en la Posición",busqueda_fruta)

    except ValueError:
        print(f"La Fruta '{ingresarfruta}' No se encuentra en la Lista")

def ejercicio3():
    total = 0
    notas = [1, 10, 5, 8, 6, 7, 4, 7, 9, 8]
    for x in range(0, len(notas)):
        total = (total + notas[x])
        print(total)
    print("El Promedio es",total/10)

def ejercicio4():
    temperaturas = [15, 27, -8, -15, 30, -2]
    max_temp = -100
    min_temp = 100
    for temperaturamaxima_actual in temperaturas:
        if temperaturamaxima_actual > max_temp:
            max_temp = temperaturamaxima_actual

    for temperaturaminima_actual in temperaturas:
        if temperaturaminima_actual < min_temp:
            min_temp = temperaturaminima_actual

    minima = temperaturas.index(min_temp)
    maxima = temperaturas.index(max_temp)
    print(f"""La Temperatura mínima es de {min_temp}°C Y se encuentra en la posición {minima}""")
    print(f"La Temperatura máxima es de {max_temp}°C Y se encuentra en la posición {maxima}""")

def ejercicio5():
    numeros_lista = [1, 10, 6, 8, 9, 4]
    numeros_lista.sort()
    print(numeros_lista)

def ejercicio6():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares = []
    impares = []
    for x in range(1, len(numeros) + 1):
        if (x % 2) == 0:
            pares.append(x)
    print("Los Números Pares son:",pares)
    for x in range(1, len(numeros) + 1):
        if (x % 2) != 0:
            impares.append(x)
    print("Los Números Impares son:",impares)

def menu():
    opc = int(input("""Elegí uno de los ejercicios travieso 
        Ejercicio 1: Carga y Recorrido Básico
        Ejercicio 2: Búsqueda y Conteo
        Ejercicio 3: Suma y Promedio 
        Ejercicio 4: Encontrar el Valor Máximo y Mínimo
        Ejercicio 5: Ordenamiento
        Ejercicio 6: Pares e Impares
        elección: """))
    while opc != 0:
        if opc == 1:
            ejercicio1()
            break
        elif opc == 2:
            ejercicio2()
            break
        elif opc == 3:
            ejercicio3()
            break
        elif opc == 4:
            ejercicio4()
            break
        elif opc == 5:
            ejercicio5()
            break
        elif opc == 6:
            ejercicio6()
            break
menu()

