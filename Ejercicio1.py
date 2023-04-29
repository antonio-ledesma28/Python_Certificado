#1 Programa que pida 2 números y muestre  la suma, resta, la multilicacipón y la división de ellos

print("Programa que pida 2 números y muestre  la suma, resta, la multilicacipón y la división de ellos")
x = int(input("Ingresa el primer número: "))
y = int(input("Ingresa el segundo número: "))

sum = x + y 
res = x - y
mult = x * y

print("\nLos números son: " , x , " y" , y)
print("\nLa suma es: " , sum)
print("La resta es: " , res)
print("La multiplicación es: " , mult)

if(y == 0):
    print("No se puede dividir entre 0")
else:
    div = x / y
    print("La división es: " , div)

fin = input("Presiona enter para salir")



#2 Programa que pida un radio y calcule el perímetro y el área de un círculo
#Perímetro = 2(pi) por radio.
#Área = pi por radio al cuadrado.
print("\n")
print("Programa que pida un radio y calcule el perímetro y el área de un círculo")
radio = float(input("Ingresa el radio del círculo: "))

pi = 3.1416
per = 2*pi*radio
area = pi*radio**2

print("El perímetro del círculo es: " , per)
print("El área del círculo es: " , area)
fin = input("Presiona enter para salir")



#3 Farenhein a Celcisu
print
print("Programa que transforma grados Fahrenheit A Celcius")
f = float(input("Ingresa los grados Fahrenheit: "))

c = (f - 32)*(5/9)
print(f ,"°F es igual a " , c , "°C")



#4 Media de 3 números
print
print("Programa para calcular media de 3 número")
n1 = float(input("Ingresa primer número: "))
n2 = float(input("Ingresa segundo número: "))
n3 = float(input("Ingresa tercer número: "))

m = (n1+n2+n3)/3
print("La media es: " , m)



#5 Perímetro y área de un rectángulo dada su base y altura
print
print("\nPrograma para calcular perímetro y área de un rectángulo dadas la base y la altura")
b = float(input("Ingresa la base del rectángulo: "))
h = float(input("Ingresa la altura del rectángulo: "))

p = 2*(b+h)
a = b*h
print("La base es: " , b , "La altura es: " , h)
if(b == h):
    print("La figura es un cuadrado")
print("El perímetro es: " , p , "El área es: " , a)


