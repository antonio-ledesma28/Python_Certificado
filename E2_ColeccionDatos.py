"""Crea una lista e inicializarla con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla."""

l1 = []
l2 = []
 #LISTA ORDENADA
for i in range(5):
    x = str(input("Ingresa la cadena: "))
    l1.append(x)
print(l1)

#LISTA INVERSA
for x in l1[::-1]:
    l2.append(x)

print(l2)