import time
import random
def ejercicio1():
    plata_usuario = 1000
    seguimos = True
    while seguimos == True:
        try:
            opc = int(input("""Elegí una Opción:
            1. Depositar Dinero
            2. Retirar Dinero
            3. Salir : """))
            if opc == 1:
                opc2 = int(input("Ingrese el Monto a Depositar: "))
                plata_usuario += opc2
                print("Su Monto bancario ahora es de",plata_usuario)
            elif opc == 2:
                opc3 = int(input("Ingrese el Monto a Retirar: "))
                if opc3>plata_usuario:
                    print("El Monto Escrito es mayor al Saldo Disponible, Inténtelo de Nuevo: ")
            elif opc == 3:
                print("Saliendo del Programa...")
                time.sleep(1)
                seguimos = False

        except(ValueError, TypeError):
            print("Valor Incorrecto o Suma Inválida, Inténtelo de Nuevo: ")


def ejercicio2():
    IMC = 0
    seguimos = True
    while seguimos == True:
        try:
            peso = int(input("Ingrese su Peso: "))
            altura = float(input("Ingrese su Altura: "))
            IMC = peso/(altura * altura)
            print("Su Índice de Masa Corporal es:",IMC)
            seguimos = False

        except(ValueError, TypeError):
            print("Valor Incorrecto o Suma Inválida, Inténtelo de Nuevo: ")


def ejercicio3():
    vocales = ["a","e","i","o","u"]
    seguimos = True
    while seguimos:
        try:
            frase = input("Ingrese una Frase: ")
            if frase == "agusfortnite2008":
                print("Nooo todo menos esoo")
                seguimos = False
            else:
                for vocales_a_buscar in range(0, len(vocales)-1):
                    vocal_aleatoria = random.randint(0, 4)
                    frase = frase.replace(vocales[vocales_a_buscar], vocales[vocal_aleatoria])
                print(frase)
        except ValueError:
            print("Valor Inválido, Inténtelo de Nuevo: ")

def ejercicio4():
    seguimos = True
    frase_invertida=""
    while seguimos:
            palabras_separadas = []
            frase = input("ingrese una frase: ")
            palabras_separadas = frase.split()
            print(palabras_separadas)
            for x in range(0, len(palabras_separadas)):
                palabras_separadas[x] = palabras_separadas[x][::-1]
            frase_invertida +=" ".join(palabras_separadas)
            print(frase_invertida)
ejercicio4()



def ejercicio5():
    seguimos = True
    while seguimos:
        nombres = ["Bruno","Chechon","Alan",""]