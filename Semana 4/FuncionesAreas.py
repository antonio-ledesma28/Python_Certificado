import os

#Funciones
def areaRectangulo(b,h):
    a = b * h
    return a
def areaCuadrado(l):
    a = l*2
    return a

def areaCirculo(r):
    a = 3.1416 * (r**2)
    return a


#Bucle de opciones
while True:
    print("Calculadora de áreas")
    print("1- Área de un rectángulo")
    print("2- Área de un cuadrado")
    print("3- Área de un círculo")
    print("4- Salir")
    
    entrada = int(input("Ingresa la opción deseada: "))
    os.system("cls")
    
#Condicionales
    if(entrada == 1):
        num1 = int(input("Ingresa la base del rectángulo: "))
        num2 = int(input("Ingresa la altura del rectángulo: "))
        a = areaRectangulo(num1, num2)
        print("El área del rectángulo es: ", a)
        
    elif(entrada == 2):
        num1 = int(input("Ingresa un lado del cuadrado: "))
        a = areaCuadrado(num1)
        print("El área del cuadrado es: ", a)
        
    elif(entrada == 3):
        num1 = int(input("Ingresa el radio del círculo: "))
        a = areaCirculo(num1)
        print("El área del círculo es: ", a)
       
    elif(entrada == 4):
        input("Saliendo del programa. Presiona cualquier tecla...")
        break
    
    else:
        print("Valor fuera de rango. Ingresa un valor válido")
    
    print()