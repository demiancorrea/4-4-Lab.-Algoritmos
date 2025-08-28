import time
def ejercicio1():
   matriz = [[4, 7, 1],
            [2, 9, 3],
            [9, 5, 6]]
   for fila in matriz:
      print(fila)


def ejercicio2():
   suma = 0
   matriz2 =  [[10, 30, 25],
               [65, 15, 90],
               [80, 45, 55]]
   for fila in matriz2:
       print(fila)
       for numero in fila:
           suma += numero
   print(f"La suma total de todos los números en la Matriz es: {suma}")




def ejercicio3():
   seguimos = True
   matriz3 = [[4, 7, 1],
             [2, 9, 3],
             [9, 5, 6],
             [5, 1, 9]]
   for fila in matriz3:
       print(fila)
   while seguimos:
       try:
           fila_a_encontrar = int(input("Ingrese qué fila quiere seleccionar: "))
           columna_a_encontrar = int(input("Ingrese la columna que quiere seleccionar: "))
           print("El Número encontrado en la Matriz es: ",matriz3[fila_a_encontrar][columna_a_encontrar])
           seguimos = False
       except ValueError:
           print("Valor Incorrecto, Inténtelo de Nuevo")
           seguimos = True


def ejercicio4():
   matriz4 = [[7, 1, 1],
              [6, 8, 3],
              [9, 5, 4],
              [2, 7, 3]]
   numero_mas_grande = 0
   for fila in matriz4:
       print(fila)
       for numero in fila:
           if numero > numero_mas_grande:
               numero_mas_grande = numero
   print(f"El Número Más grande es {numero_mas_grande}")


def menu():
   seguimos = True
   while seguimos:
      opc = int(input("""Elegí una Opción travieso
      Ejercicio 1(Impresión de Matriz 3x3)
      Ejercicio 2(Suma total de Matriz 3x3)
      Ejercicio 3(Búsqueda de Número Matriz 4x4)
      Ejercicio 4(Número Más grande de la Matriz 4x4)
      5 = Salir: """))
      if opc == 1:
         ejercicio1()
         time.sleep(1)
      elif opc == 2:
         ejercicio2()
         time.sleep(3)
      elif opc == 3:
         ejercicio3()
      elif opc == 4:
         ejercicio4()
         time.sleep(2)
      elif opc == 5:
          break
      else:
         seguimos = True
   return
menu()
