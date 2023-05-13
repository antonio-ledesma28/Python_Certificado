#2 Programa que pida 2 números y muestre  la suma, resta, la multilicacipón y la división de ellos

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