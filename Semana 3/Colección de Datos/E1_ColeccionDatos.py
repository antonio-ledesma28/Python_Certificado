#Ejercicio 1 Colección de dato
"""Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo."""
#Se importa biblioteca
import random

#Se crea lista vacía
l1 = []


"""Impresión sin for
#Método para crear números aleatorios
x = random.randint(1,10)
#Método para agregar un valor en el índice
l1.append(x)
x = random.randint(1,10)
l1.append(x)
x = random.randint(1,10)
l1.append(x)
x = random.randint(1,10)
l1.append(x)
x = random.randint(1,10)
l1.append(x)
x = random.randint(1,10)
l1.append(x)
x = random.randint(1,10)
l1.append(x)
x = random.randint(1,10)
l1.append(x)
x = random.randint(1,10)
l1.append(x)
print(l1)
"""
#Impresión utilizando for
"Con for"
for i in range(10):
    x = random.randint(1,10)
    l1.append(x)

#Impresión lista 10 elementos aleatorios
print(l1)

#While
l2 = []
i = 0
print("Con while")
while (i<10):
    x = random.randint(1,10)
    l2.append(x)
    i = i+1
print(l2)

#Muestra cada elemento con su cuadrado y su cubo 3
print("Elemento, cuadrado y cúbica")
for elemento in l1:
    print(elemento, elemento**2,elemento**3) 