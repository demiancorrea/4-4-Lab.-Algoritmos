def ejercicio1():
   try:
      num1 = int(input("Ingrese un Número: "))
      num2 = int(input("Ingrese un Segundo Número: "))
      resultado = num1/num2
      print(resultado)
   except ZeroDivisionError:
      print("No se Puede dividir por cero pedazo de fracaso")
   finally:
      print("Jaja Balatro")

def ejercicio2():
   seguimos = True
   while seguimos == True:
      try:
         edad = int(input("Qué edad tenés?: "))
         seguimos = False

      except ValueError:
         print("Valor Incorrecto, Inténtalo de Nuevo")
         seguimos = True

def ejercicio3():
   seguimos = True
   while seguimos == True:
      try:
         nombres = ["Ana", "Pedro", "Sofía"]
         indice = int(input("Ingresa un Índice del 0 al 2: "))
         print(nombres[indice])
         seguimos = False
      except (IndexError,ValueError):
         print("Valor Incorrecto o Índice Fuera de Rango, Inténtalo de nuevo")
         seguimos = True

def ejercicio4():
   seguimos = True
   while seguimos == True:
      try:
         num1 = int(input("Ingrese un Número: "))
         num2 = int(input("Ingrese un Segundo Número: "))
         result = num1 + num2
         print(result)
         seguimos = False
      except (ValueError,TypeError):
         print("Valor Incorrecto o Error en la suma de los números, Inténtelo de nuevo")
         seguimos = True

def ejercicio5():
      try:
         num1 = int(input("Ingrese un Número: "))
         num2 = int(input("Ingrese un Segundo Número: "))
         resultado = num1/num2
         print(resultado)
      except (ZeroDivisionError,ValueError):
         print("Valor Incorrecto o No se puede dividir Por 0, Intentalo de Nuevo")

      finally:
         print("Fin del programa de cálculo")

def menu():
   seguimos = True
   while seguimos == True:
      opc = int(input("""Elegí una Opción travieso
      Ejercicio 1(División)
      Ejercicio 2(Edad)
      Ejercicio 3(Listas)
      Ejercicio 4(Suma)
      Ejercicio 5(División con Finally): """))
      if opc == 1:
         ejercicio1()
      elif opc == 2:
         ejercicio2()
      elif opc == 3:
         ejercicio3()
      elif opc == 4:
         ejercicio4()
      elif opc == 5:
         ejercicio5()
      else:
         seguimos = True
   return
menu()