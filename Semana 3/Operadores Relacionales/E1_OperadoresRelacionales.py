"""Programa que imprima si el número es positivo o negativo."""

x = int(input("Ingresa un número: "))

if(x > 0):
    print("El número: ", x, " es positivo")
elif(x < 0):
    print("El número: ", x, " negativo")
else:
    print("El número es 0")