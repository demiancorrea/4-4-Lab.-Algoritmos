def generacion_mazo():
    mazo_52x2 = []
    acumulador_de_chips = 0
    num_cartas = 52
    palos = ["Corazones",
             "Diamantes",
             "Tréboles",
             "Picas"]
    numero_carta = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    for mazo in range(0,1):
        lista_aux = []
        for x in range(0,len(palos)):
            lista_aux.append(palos[x])
            for y in range(0,len(numero_carta)):
                if numero_carta[y] == 1 or 11 or 12 or 13:
                    if numero_carta[y] == 1:
                        lista_aux.append("A")
                        acumulador_de_chips += 11
                    elif numero_carta[y] == 11:
                        lista_aux.append("J")
                        acumulador_de_chips += 10
                    elif numero_carta[y] == 12:
                        lista_aux.append("Q")
                        acumulador_de_chips += 10
                    elif numero_carta[y] == 13:
                        lista_aux.append("K")
                        acumulador_de_chips += 10
                    else:
                        lista_aux.append(numero_carta[y])
                        acumulador_de_chips += numero_carta[y]
        mazo_52x2.append(lista_aux)
        print(mazo_52x2)
    print(f"El total de los chips del mazo es de {acumulador_de_chips} chips")
generacion_mazo()