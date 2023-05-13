#Realizar un ejemplo de menú, donde podemos escoger las distintas opciones 
#hasta que seleccionamos la opción de “Salir”.
import os
#Funciones
def sumar(a, b):
    return a + b

while True:
    print("Elige una opción")
    print("MENU")
    print("1. Imprime tu nombre")
    print("2. Suma 2 números")
    print("3. Calcula el area de un círculo")
    print("4. Identifica el mayor de 2 números ingresados por el usuario")
    print("5. Salir")
    
    x = int(input("Ingresa la opción: "))
    os.system("cls")
    
    if x == 1:
        nombre = str(input("Ingresa tu nombre: "))
        print("Hola", nombre)
        
    elif x  == 2:
        n1 = int(input("Ingresa el primer número a sumar: "))
        n2 = int(input("Ingresa el segundo número número a sumar: "))
        n3 = sumar(n1, n2)
        print("La suma del " , n1, " más " , n2, " es: ", n3)
        
    elif x  == 3:
        r = int(input("Ingresa el radio del círculo a calcular: "))
        a = 3.1416 * (r**2)
        print("El área del círculo es: ", a)
        
    elif x  == 4:
        n1 = int(input("Ingresa el primer número: "))
        n2 = int(input("Ingresa el segundo número número: "))
        if(n1 > n2):
            print("El primero número es mayor. ", n1, " es mayor que " , n2)
        else:
            print("El segundo número es mayor. ", n2, " es mayor que " , n1)
            
    elif x  == 5:
        break
    
    else:
        print("Opción fuera de rango")
    print("")
print("Fin del programa")