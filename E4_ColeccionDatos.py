"""Codifica un programa en Python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listados con las notas de cada alumno.

El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error."""
grupo = []
alumno = []
calificacion = []
aux = -1
while(aux==0):
    x = str(input("Ingresa el nombre de el alumno: "))
    for i in alumno:
        print()
        

diccionario = {"Antonio", "Juan"}
