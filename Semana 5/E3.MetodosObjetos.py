'''
Vamos a crear un programa en Python donde vamos a declarar un diccionario 
para guardar los precios de las distintas frutas. El programa pedirá el nombre 
de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la 
fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. 
Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.
'''

f = {"Manzana": 5, "Uva": 0.3, "Melón": 15.6, "Mango": 2}
while True:
    fruta = str(input("Ingrese fruta: "))
    fruta2 = fruta.capitalize()
    cantidad = float(input("Ingresa cantidad en númerico: "))

    if fruta2 in f:
        print (f[fruta2]*cantidad)
    else:
        print("Fruta no existe")

    opc = str(input("\nInserta 0 para salir o enter para otra consulta: "))
    if(opc == "0"):
        break
    else:
        pass
