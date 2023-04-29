"""Crea una tupla con los meses del año, pide números al usuario, si el número está entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero."""

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

i = -1
aux = 0
print("Introduce el número del mes\n","El programa termina al introducir 0 ")
#While para ciclo de programa
while (i!=0):
    x = int(input("Introduce un número del 1 al 12 para darte un mes: "))
    #Calculo del mes
    if(x<=12 and x>0):
        print("El mes es: ", meses[x-1])

    #Cierre de programa
    elif x == 0:
        print("Fin del programa")
        i=0
    #Número no válido
    else:
        print("El valor introducido no es válido. Vuelve a ingresar")
