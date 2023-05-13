#Crea una aplicación que pida un número y calcule su factorial 
# (El factorial de un número es el producto de todos los enteros entre 1 
# y el propio número y se representa por el número seguido de un signo de exclamación. 
# Por ejemplo 5! = 1x2x3x4x5=120).
import os

#Se pide el número a sacar el factor
num = int(input("Ingresa un número entero para calcular su factorial: "))
#Se crea unn acumulador
acum = 1
#Bucle para todas las iteraciones
for i in range(num-1):
    acum = acum * (i+2)
    #print(acum)
    
print("Factorial de ", num, ": ", acum)