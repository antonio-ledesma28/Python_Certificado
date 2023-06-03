'''
Escribe un programa que lea una cadena y devuelva un diccionario 
con la cantidad de apariciones de cada carácter en la cadena.
'''



cadena = str(input("Ingresa cadena: "))

cad = {}

for i in cadena:
    if i in cad:
        cad[i] = cad[i] + 1
    else:
        cad[i] = 1
print(cad)

#Item
for clave, valor in cad.items():
    print(clave, "->", valor)