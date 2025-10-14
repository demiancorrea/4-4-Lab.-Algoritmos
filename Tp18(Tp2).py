import random
intentos = 7
palabras = ["computadora", "tecnología"]
palabra_= []
palabra_elegida = random.choice(palabras)
for x in range(len(palabra_elegida)):
    palabra_.append("_")
while intentos>0:
    print(f"{palabra_} intentos restantes: {intentos}")
    letra_elegida=input("ingrese la letra elegida:")
    adivino=False
    for indice_letra in range (len(palabra_elegida)):
        for letra2 in letra_elegida:
            if letra2==palabra_elegida[indice_letra]:
                palabra_[indice_letra]=letra2
                adivino=True
    if not adivino:
        intentos-=1
    if not "_" in palabra_:
        print("ganaste sos un chad.")
        break
if intentos<=0:
    print("perdiste bobo.")

with open('palabras jugadas', 'w', encoding='utf-8') as archivo:
   archivo.write("Las palabras jugadas son:\n")
   archivo.write(palabra_elegida)

print("¡Archivo 'palabras jugadas' creado con éxito!")