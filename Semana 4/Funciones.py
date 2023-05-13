import os

def sumar(a, b):
    print(a + b)
    
def saluda():
    print("Hola desde la función saluda")
    
    
def saludaConNombre(nombre):
    print("Hola:", nombre)
    
def multiplicar(a, b, c):
    return a* b* c

#------------------------------------------
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def ingPrimNumero():
    a = int(input("Ingresa primer número: "))
    return a

def ingSegNumero():
    a = int(input("Ingresa primer número: "))
    return a
    
#Zona de invocación
'''sumar(4, 7)
sumar(45, 27)
saluda()
saludaConNombre("Antonio")
a = multiplicar(1, 5, 7)
print(a)'''

while True:
    print("Calculadora básica")
    print("1- Suma 2 números")
    print("2- Resta 2 números")
    print("3- Multiplica 2 números")
    print("4- Divide 2 números")
    print("5- Salir")
    
    opc = int(input("Elige opción: "))
    
    if opc == 1:
        x1 = ingPrimNumero()
        x2= ingSegNumero()
        x =suma(x1,x2)
        print("La suma es: " , x)
        
    elif opc == 2:
        x1 = ingPrimNumero()
        x2= ingSegNumero()
        x =resta(x1,x2)
        print("La resta es: " , x)
        
    elif opc == 3:
        x1 = ingPrimNumero()
        x2= ingSegNumero()
        x =mult(x1,x2)
        print("La multiplicación es: " , x)
        
    elif opc == 4:
        x1 = ingPrimNumero()
        x2= ingSegNumero()
        x =div(x1,x2)
        print("La división es: " , x)
    
    if opc == 5:
        break
    print()