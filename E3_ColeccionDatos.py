"""Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor."""
 #Todas las notas y cálculo de la media
l1 = []
i = 0
media = 0
alta = 0
baja = 10
while (i<5):
    print("Ingresa la calificación del alumno " , i+1)
    x = int(input())
    if(x < 10 and x > 0): 
        l1.append(x)
        #Se suman valores para la media
        media = media + x
        #Alta
        if alta < x:
            alta = x
        #Baja
        if x < baja:
            baja = x;
        i = i+1   
                
    else:
        print("El valor no es válido, ingresa de nuevo") 
        

todas = l1
media = media/5

print("Todas las notas: ", todas)
print("Nota media: ", media)
print("Nota más alta: ", alta)
print("Nota más baja ", baja)

