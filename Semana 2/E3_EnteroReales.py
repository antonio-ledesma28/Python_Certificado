#3 Perímetro y área de un rectángulo dada su base y altura
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


