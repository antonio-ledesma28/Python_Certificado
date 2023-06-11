#Se realiza conexión con los otros dos archivos en el main
from Palabras import dict
from Ahorcado_Diagramas import diagramas
#Se importa biblioteca Random
import random

#Guarda número al azar del 1 al 4
numeroAzar = random.randint(1,4)
#Guarda en una variable el color dependiendo el número al azar
palabraOculta = dict[numeroAzar].lower()
#print(palabraOculta)

print("Juego del ahorcado")
print("Adivina la palabra oculta")
print("Tienes 7 intentos")

#Función para poder separar letra por letra en un arreglo
letras = set(palabraOculta)
print(len(letras))

vidas = 7
dibujo = 0

while vidas != 0 and len(letras) != 0:    
    #print(letras)
    letraIngresada = str(input("Ingresa letra:")).lower()

    if letraIngresada in letras:
        if(len(letras) != 0):
            print("Acertaste")
            letras.remove(letraIngresada)
            print(letras)
        else:
            print("FELICIDADES. Adivinaste la palabra: ", palabraOculta)

    else:
        print(diagramas[dibujo])
        dibujo = dibujo + 1
        vidas = vidas - 1
        if(vidas > 1):
            print("Fallastes, te quedan sólo ", vidas, "vidas")
        if (vidas == 1):
            print("Fallastes, te queda sólo ", vidas, "vida")

if vidas == 0:
    print("FALLASTE. GAME OVER")

if (len(letras) == 0):
    print("FELICIDADES, GANASTE, LA PALABRA CORRECTA ERA:",palabraOculta.capitalize())


"""
palabra = str(input("Ingresa palabra: "))
if palabra == palabraOculta:
    print("Acertaste")
else:
    print("Fallaste")
"""
