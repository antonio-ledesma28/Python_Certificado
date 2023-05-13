"""Programa que imprima si el número ingresado esta en el rango de 1 a 7."""

x = int(input("Ingresa un número: "))

if(x <= 7 and x >= 1):
    print("El número ", x, " está en el rango de [1,7]")

else:
    print("El número ", x, " está fuera del rango [1,7]")