#Encapsulamiento
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nombre):
        self.__nombre = nombre

    def getEdad(self):
        return self.__edad
    
    def setEdad(self,edad):
        self.__edad = edad
    


q1 = Persona("Copernico", 45)

#Impresión primeros valores
print(q1.getNombre())
print(q1.getEdad())

#Cambia valores
q1.setNombre("Juan")
q1.setEdad(30)

#Impresión segundos valores
print(q1.getNombre())
print(q1.getEdad())