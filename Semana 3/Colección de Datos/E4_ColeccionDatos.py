# Creamos un diccionario vacío donde guardaremos los alumnos y sus notas
alumnos = {}

# Pedimos al usuario que introduzca el número de alumnos que va a registrar
num_alumnos = int(input("Introduce el número de alumnos: "))

# Iteramos por cada alumno
for i in range(num_alumnos):
    # Pedimos al usuario que introduzca el nombre del alumno
    nombre = input(f"Introduce el nombre del alumno {i+1}: ")
    
    # Creamos una lista vacía para las notas del alumno
    notas = []
    
    # Pedimos al usuario que introduzca las notas del alumno hasta que introduzca un número negativo
    nota = float(input("Introduce una nota (introduce un número negativo para salir): "))
    while nota >= 0:
        notas.append(nota)
        nota = float(input("Introduce otra nota (introduce un número negativo para salir): "))
    
    # Comprobamos si el nombre del alumno ya ha sido registrado
    if nombre in alumnos:
        print(f"Error: el alumno {nombre} ya existe")
    else:
        # Guardamos el nombre y las notas del alumno en el diccionario
        alumnos[nombre] = notas

# Mostramos por pantalla el listado de alumnos y sus notas, así como su media
print("\nListado de alumnos y sus notas:")
for nombre, notas in alumnos.items():
    media = sum(notas) / len(notas)
    print(f"{nombre}: {notas}, media = {media}")