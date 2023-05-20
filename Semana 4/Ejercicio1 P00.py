#Crear una clase llamada alumnos con aributos, nombres, apellido paterno, materno y calificación o nota, creando 5 objetos
'''
class Alumnos:
    def __init__(self, nombre, aPaterno, aMaterno, calificacion):
        self.nombre = nombre
        self.aPaterno = aPaterno
        self.aMaterno = aMaterno
        self.calificacion = calificacion

        
    #Zona de invocación
    primero = Alumnos("Antonio", "Ledesma", "Briones", 10)
    '''

class alumnos:
    def __init__(self, nombre, aPaterno, aMaterno, calificacion):
        self.nombre = nombre
        self.aPaterno = aPaterno
        self.aMaterno = aMaterno
        self.calificacion = calificacion
    def imprime(self):
        print(self.nombre, self.aPaterno, self.aMaterno, self.calificacion)


    def aprobo(self):
        if self.calificacion > 6:
            print("El alumno: ", self.nombre, " APROBÓ con una calificación de: ", self.calificacion)
        else:
            print("El alumno: ", self.nombre, " REPROBÓ con una calificación de: ", self.calificacion)

#zona de invocación
primero = alumnos("Antonio", "Ledesma", "Briones", 10)
segundo = alumnos("Juan", "Sánchez", "Flores", 4)
tercero = alumnos("Carlos", "Soís", "Díaz", 8)
cuarto = alumnos("Elian", "González", "Reyes", 10)
quinto = alumnos("Kevin", "Hernández", "Sánchez", 5)
'''
print("\nImpresión de los datos de cada objeto\n")
print(primero.nombre, primero.aPaterno, primero.aMaterno, primero.calificacion)
print(segundo.nombre, segundo.aPaterno, segundo.aMaterno, segundo.calificacion)
print(tercero.nombre, tercero.aPaterno, tercero.aMaterno, tercero.calificacion)
print(cuarto.nombre, cuarto.aPaterno, cuarto.aMaterno, cuarto.calificacion)
print(quinto.nombre, quinto.aPaterno, quinto.aMaterno, quinto.calificacion)
'''

primero.imprime()
segundo.imprime()
tercero.imprime()
cuarto.imprime()
quinto.imprime()
print()
primero.aprobo()
segundo.aprobo()
tercero.aprobo()
cuarto.aprobo()
quinto.aprobo()