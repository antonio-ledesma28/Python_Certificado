#Colecciones de datos

#LISTA
#Lista se puede modificar
#índice   0 1 2 3 4
lista1 = [1,2,3,4,5]

#Imprime el número en el índice 4
print(lista1[4])
#Imprime el primer número a la derecha
print(lista1[-1])

#Lista de datos de diferente tipo
lista2 = ["Hola", True, 5.678, -8, "Mundo"]
#Concatenación de dos elementos
print(lista2[0], lista2[4])

#Sublistas
lista3 = [8, 53, [1,2,3], 98, 56]
#Se imprime el valor en el índice 2 que es otra lista
print(lista3[2])

#Muestra el tipo de dato (Lista)
print(type(lista1))


#TUPLA
#Tupla no se puede modificar
tupla = (45,36,68,9)
print(type(tupla))
print(tupla[2])

#Modificación lista
lista1[2] = "Copernico"
print(lista1)

#Error
"""tupla[0] = 46
print(tupla)"""


#DICCIONARIO
"Primer elemento llave y segundo valor asociado"
diccionario1 = {"A":"Hola", 31:True, 4:3.15}
print(diccionario1)
#Se imprime valor a través de la llave
print(diccionario1["A"])

#Visualiza las llaves del diccionario
print(diccionario1.keys())
#Cambia el valor del dato a través de su llave
diccionario1[31] = False
print(diccionario1)

