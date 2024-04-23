#juegoDePalabras
#juegoRandom

print("------holaa--------")
print()
totalPalabras = int(input("cuantas palabras? "))

print()

historialPalabras = ""

for cualpalabra in range(1, (totalPalabras + 1)):
    p1 = input("palabra para el jugador1: ")
    historialPalabras +=" "
    historialPalabras += p1

    p2 = input("parabra para el jugador2: ")
    historialPalabras += " "
    historialPalabras += p2

    print()
    print("Story: " + historialPalabras)
